from setuptools import setup
from codecs import open

from Afvalwijzer import Afvalwijzer

# Packaging
# https://packaging.python.org/tutorials/distributing-packages/
# classifiers
# https://pypi.python.org/pypi?%3Aaction=list_classifiers

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

with open('HISTORY.md', 'r', 'utf-8') as f:
    history = f.read()

setup(name='afvalwijzer',
      version=Afvalwijzer.__version__,
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
      install_requires=['requests', 'beautifulsoup4', 'datetime'],
      include_package_data=True,
      # python_requires='>=2.7.0, >=3.4.0, <4',
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      zip_safe=False)
