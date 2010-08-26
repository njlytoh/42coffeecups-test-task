from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='project',
      version=version,
      description="42CoffeeCups test project from njlytoh",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='django project simple',
      author='Andriy Tomchuk',
      author_email='andrij.tomchuk@gmail.com',
      url='http://atomchuk.user.eksi.net/',
      license='',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=[],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
