from setuptools import setup
from codecs import open
import os
import re

# Packaging
# https://packaging.python.org/tutorials/distributing-packages/
# classifiers
# https://pypi.python.org/pypi?%3Aaction=list_classifiers

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

with open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()

setup(name='afvalwijzer',
      version=find_version("Afvalwijzer", "__init__.py"),
      description='Getting the waste date and type for the Netherlands',
      long_description=readme + '\n\n' + history,
      url='https://github.com/bambam82/afvalwijzer',
      author='Bart Dorlandt',
      author_email='bart@bamweb.nl',
      license='MIT',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Other Audience',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Natural Language :: English',
          'Natural Language :: Dutch',
          'License :: OSI Approved :: MIT License',
          'Operating System :: Unix',
          'Operating System :: MacOS',
          'Operating System :: Microsoft :: Windows',
          'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      keywords='afval afvalwijzer garbage',
      packages=['Afvalwijzer'],
      install_requires=['requests', 'beautifulsoup4'],
      include_package_data=True,
      # python_requires='>=2.7.0, >=3.4.0, <4',
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      zip_safe=False)
