import setuptools

requires = [
    "flake8 > 3.0.0",
]

setuptools.setup(
    name="flake8_vyper",
    license="MIT",
    version="0.1.0",
    description="Plugin for flake8 to support Vyper",
    author="Mike Shultz",
    author_email="mike@mikeshultz.com",
    url="https://gitlab.com/mikeshultz/flake8-vyper",
    py_modules=['flake8_vyper'],
    install_requires=requires,
    entry_points={
        "flake8.report": [
            'vyper_filter = vyper_filter:VyperFilterPlugin',
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
