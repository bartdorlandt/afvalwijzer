from setuptools import setup

# Packaging
# https://packaging.python.org/tutorials/distributing-packages/
# classifiers
# https://pypi.python.org/pypi?%3Aaction=list_classifiers

setup(name='afvalwijzer',
      version='0.1',
      description='Getting the waste date and type for the Netherlands',
      url='https://github.com/bambam82/afvalwijzer',
      author='Bart Dorlandt',
      author_email='bart@bamweb.nl',
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
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
      python_requires='>=2.7.*, >=3.4.*, <4',
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      zip_safe=False)
