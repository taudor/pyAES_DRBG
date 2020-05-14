## -*- encoding: utf-8 -*-
import os
import sys
from setuptools import setup, find_packages

setup(
    name="aes_drgb",
    version="0.0.1",
    description="AES DRGB SP 800-90A, Rev 1 NIST",
    long_description="AES DRGB SP 800-90A, Rev 1 NIST",
    author="Tudor A. A. Soroceanu",
    author_email="tudor.soroceanu@aisec.fraunhofer.de",
    url="https://github.com/taudor/pyAES_DRBG",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Security :: Cryptography',
    ],
    keywords="AES",
    packages=find_packages(),
    python_requires='>3',
)
