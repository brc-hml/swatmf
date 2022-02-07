from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.5'
DESCRIPTION = 'swatmf is a set of python modules for SWAT-MODFLOW model'
LONG_DESCRIPTION = 'A package that allows to work with SWAT-MODFLOW model'

license = "BSD-3-Clause"
# Setting up
setup(
    name="swatmf",
    version=VERSION,
    author="Seonggyu Park",
    author_email="<envpsg@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    download_url="https://pypi.org/project/swatmf",
    project_urls={
        "Bug Tracker": "https://github.com/spark-brc/swatmf/issues",
        "Source Code": "https://github.com/spark-brc/swatmf",
        "Documentation": "https://github.com/spark-brc/swatmf",
    },


    # include_package_data=True,
    package_data = {
        'opt_files': ['*'],
    },
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'pyemu', 'matplotlib','hydroeval', 'tqdm', 'termcolor'],
    keywords=['python', 'SWAT-MODFLOW', 'PEST'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: BSD License"
    ]
)