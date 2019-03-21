from flake8.formatting.default import Default

__author__ = 'Mike Shultz'
__email__ = 'mike@mikeshultz.com'
__version__ = '0.1.0'


class VyperFilterPlugin(Default):
    """ flake8 formatter plugin to filter false-positive errors for Vyper """
    name = 'vyper_filter'
    version = __version__

    vyper_types = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._assemble_vyper_types()

    def _assemble_vyper_types(self):
        bit_lengths = ['256', '128', '64', '32', '16', '8', '4', '2', '1']
        types_with_length = ['bytes', 'uint', 'int']
        unique_types = ['address', 'string']
        self.vyper_types = ['{}{}'.format(t, l) for t in types_with_length for l in bit_lengths]
        self.vyper_types += unique_types

    def _default_format(self, error):
        return Default.error_format % {
            "code": error.code,
            "text": error.text,
            "path": error.filename,
            "row": error.line_number,
            "col": error.column_number,
        }

    def _contains_type(self, error):
        return any([t in error.text for t in self.vyper_types])

    def _contains_interface_bodyless(self, error):
        return any([m in error.text for m in ['constant', 'modifying']])

    def _contains_visibility(self, error):
        return any([m in error.text for m in ['public', 'private']])

    def _contains_global(self, error):
        return any([m in error.text for m in ['self', 'msg']])

    def handle(self, error):
        line = self.format(error)
        if line:
            source = self.show_source(error)
            self.write(line, source)

    def format(self, error):
        if error.filename.endswith('.vy'):
            if error.code == 'F821':
                # filter out "undefined name" for vyper globals and types
                if (self._contains_type(error)
                        or self._contains_interface_bodyless(error)
                        or self._contains_visibility(error)
                        or self._contains_global(error)):
                    return

        return self._default_format(error)
