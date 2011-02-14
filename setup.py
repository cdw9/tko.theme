from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='tko.theme',
      version=version,
      description="An installable theme for Plone 4",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='web zope plone theme',
      author='Chrissy Wainwright',
      author_email='cwainwright@gmail.com',
      url='http://www.tkotaekwondo.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['tko'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins = ["ZopeSkel"],
      )
