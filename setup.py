import os

import setuptools

cffi_modules = [
    "src/_cffi_src/build_opus.py:ffibuilder",
    "src/_cffi_src/build_vpx.py:ffibuilder",
]

# Do not build cffi modules on readthedocs as we lack the codec development files.
if os.environ.get("READTHEDOCS") == "True":
    cffi_modules = []

install_requires = [
    "aioice>=0.9.0,<1.0.0",
    "av>=9.0.0,<11.0.0",
    "cffi>=1.0.0",
    "cryptography>=2.2",
    'dataclasses; python_version < "3.7"',
    "google-crc32c>=1.1",
    "pyee>=9.0.0",
    "pylibsrtp>=0.5.6",
    "pyopenssl>=23.1.0",
]

extras_require = {
    'dev': [
        'aiohttp>=3.7.0',
        'coverage>=5.0',
        'numpy>=1.19.0',
    ]
}

setuptools.setup(
    cffi_modules=cffi_modules,
    name='aiortc',
    version='1.5.0',
    package_dir={"": "src"},
    packages=["aiortc", "aiortc.codecs", "aiortc.contrib"],
    python_requires=">=3.7",
    setup_requires=["cffi>=1.0.0"],
    install_requires=install_requires,
    extras_require=extras_require,
    )
