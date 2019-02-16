"""A setuptools based setup module.
"""
import os

from setuptools import setup, find_packages
from setuptools.command.develop import develop

import py_metrics

__version__ = py_metrics.__version__

class Cache(develop):
    # Add custom build step to setup.py
    def run(self):
        develop.run(self)
        import appdirs # Import here to ensure install_requires runs
        vsrc = appdirs.user_cache_dir(
            appname=self.distribution.metadata.name,
            version=__version__)
        src = appdirs.user_cache_dir(
            appname=self.distribution.metadata.name)
        dst = os.path.join(os.path.dirname(__file__), 'cache')
        if not os.path.exists(vsrc):
            os.makedirs(vsrc)
        if not os.path.exists(dst):
            os.symlink(src, dst)


setup(
    name=py_metrics.__appname__,
    version=__version__,
    python_requires='>=3.6',
    description='Use python for econometrics',
    author='Kalu',
    author_email='kalu@121onto.com',

    cmdclass={'develop': Cache},
    packages=find_packages(exclude=['output', 'tests']),
    include_package_data=True,

    install_requires=[
        'scipy',
        'numpy',
        'pandas',
        'appdirs',
    ],

    extras_require={
        'dev': [
            'ipython',
            'sklearn',
            'matplotlib',
        ],
    },

    setup_requires=[
        'appdirs',
    ]
)