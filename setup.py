from codecs import open as codecs_open
from setuptools import setup, find_packages

# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(name='similarity-searching-sketches',
      version='0.0.2',
      description=u"Package containing implementations used in metric sketch evaluation experiments.",
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
      install_requires=[
          'pip',
          'setuptools',
          'jupyter',
          'numpy',
          'SciPy',
          'scikit-learn',
          'pandas',
          'jupyter',
          'matplotlib'
      ]
      )
