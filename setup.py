#!/usr/bin/env python3
"""
atriumOS setup configuration
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="atriumos",
    version="1.0.0",
    author="atriumOS Team",
    author_email="your.email@example.com",
    description="Universal Development Environment Setup - A modern, cross-platform setup script",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/atriumos",
    py_modules=["atriumos"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.7",
    install_requires=[
        "rich>=13.0.0",
    ],
    entry_points={
        "console_scripts": [
            "atriumos=atriumos:main",
        ],
    },
    keywords="setup development-environment cli cross-platform devtools",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/atriumos/issues",
        "Source": "https://github.com/yourusername/atriumos",
        "Documentation": "https://github.com/yourusername/atriumos/wiki",
    },
)
