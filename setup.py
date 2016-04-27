import os
from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name='little-ebay',
    version=version,
    description='auction system',
    author='Surya Rao',
    author_email='hp7h14p@gmail.com',
    url='',
    packages=find_packages(),
    zip_safe=False,
    platforms=["any"],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        ],
    )
