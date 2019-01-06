from setuptools import setup

setup(
    name="svd2zig",
    version="0.1",
    description="Generate Zig register maps and code from SVD files",
    url="https://github.com/adfernandes/svd2zig",
    author="Andrew Fernandes",
    author_email="andrew@fernandes.org",
    license="Apache License, Version 2.0",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Embedded Systems"
        "Intended Audience :: Developers",
        "Environment :: Console",
    ],
    packages=["svd2zig"],
    zip_safe=True, # https://stackoverflow.com/a/20885799
)

# Note: to include the SVD XSD file: https://stackoverflow.com/a/1857436
