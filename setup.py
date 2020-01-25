import os
import re
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='ugapi',
    version=find_version("ugapi", "__init__.py"),
    description='Ultimate-Guitar Tab API',
    url='http://github.com/doodoroma/ugapi',
    author='Adam Meszaros',
    author_email='doodoroma@gmail.com',
    license='MIT',
    packages=['ugapi'],
    install_requires=[
        'scrapy',
        'pandas'
    ],
    zip_safe=False
)
