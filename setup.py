from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(name='similarity-searching-sketches',
      version='0.0.1',
      description=u"Module for Diploma thesis on Similarity Searching on metric Sketches.",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Matej Kvassay",
      author_email='matejkvassay5@gmail.com',
      url='https://github.com/matejkvassay/similarity-searching-sketches.git',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=required,
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      pyskel=pyskel.scripts.cli:cli
      """
      )
