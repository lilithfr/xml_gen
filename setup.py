from setuptools import setup
import setuptools

# https://github.com/elgertam/cookiecutter-pypackage/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/setup.py

from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip

pfile = Project(chdir=False).parsed_pipfile
requirements = convert_deps_to_pip(pfile['packages'], r=False)
test_requirements = convert_deps_to_pip(pfile['dev-packages'], r=False)

setup(
    name='xml_gen',
    version='1.0.0',
    packages=setuptools.find_packages(),
    url='http://sqrpnt.com/sp/og/xml_gen',
    license='private',
    author='lambiale',
    author_email='',
    description='XML Config Generator',
    install_requires=requirements,
    tests_require=test_requirements
)
