# This will try to import setuptools. If not here, it will reach for the embedded
# ez_setup (or the ez_setup package). If none, it fails with a message
try:
    from setuptools import setup
except ImportError:
    try:
        import ez_setup
        ez_setup.use_setuptools()
    except ImportError:
        raise ImportError("Library could not be installed, probably because"
            " neither setuptools nor ez_setup are installed on this computer."
            "\nInstall ez_setup ([sudo] pip install ez_setup) and try again.")

from setuptools import setup, find_packages

exec(open('version.py').read()) # loads __version__

setup(name='collatz',
      version=__version__,
      url='https://github.com/NGeorgescu/' + 'collatz',
      author='NGeorgescu',
      author_email='nsgeorgescu@gmail.com',
    description='set of tools for playing around with the collatz conjecture',
    long_description=open('README.rst').read(),
    license='see LICENSE.txt',
    keywords="collatz discrete math number theory",
    packages= find_packages(exclude='docs'))
