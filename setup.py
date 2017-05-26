#!/usr/bin/env python

import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 3):
    sys.exit('Sorry, Python < 3.3 is not supported')

setup(
    name='pyecore',
    version='0.5.6-dev',
    description=('A Python(ic) Implementation of the Eclipse Modeling '
                 'Framework (EMF/Ecore)'),
    long_description=open('README.rst').read(),
    keywords='model metamodel EMF Ecore MDE',
    url='https://github.com/pyecore/pyecore',
    author='Vincent Aranega',
    author_email='vincent.aranega@gmail.com',

    packages=find_packages(exclude=['examples', 'tests']),
    # data_files=[('', ['LICENSE', 'README.rst'])],
    install_requires=['enum34;python_version<"3.4"',
                      'ordered-set',
                      'lxml'],
    tests_require={'pytest'},

    license='BSD 3-Clause',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: BSD License',
    ]
)
