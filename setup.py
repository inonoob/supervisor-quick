#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="supervisor-quick",
    version=__import__("supervisor_quick").__version__,
    description="Bypass supervisor's nasty callbacks stack and make it quick!",
    author="Lx Yu",
    author_email="i@lxyu.net",
    maintainer="Sergey Kolosov",
    maintainer_email="m17.admin@gmail.com",
    py_modules=["supervisor_quick", ],
    package_data={"": ["LICENSE"], },
    url="https://github.com/sergeykolosov/supervisor-quick",
    license="MIT",
    long_description=open("README.rst").read(),
    install_requires=[
        "supervisor",
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ]
)
