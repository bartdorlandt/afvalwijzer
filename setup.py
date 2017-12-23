from setuptools import setup

setup(name='afvalwijzer',
      version='0.1',
      description='Waste guide for the Netherlands',
      url='https://github.com/bambam82/afvalwijzer',
      keywords='afval afvalwijzer garbage',
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      author='Bart Dorlandt',
      author_email='bart@bamweb.nl',
      classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Natural Language :: English',
        'Natural Language :: Dutch',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      packages=['Afvalwijzer'],
      zip_safe=False)
