from distutils.core import setup
from setuptools import find_packages
from distutils.cmd import Command


class CoverageCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys, subprocess

        code = subprocess.call([
            sys.executable, '-m', 'nose', 'tests', '--with-coverage', '--cover-package', 'waves_gateway',
            '--cover-html'
        ])

        exit(code)


class MyPyCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys, subprocess

        code = subprocess.call([sys.executable, '-m', 'mypy', 'waves_gateway', '--ignore-missing-imports'])

        exit(code)


class LintCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys, subprocess

        code = subprocess.call([sys.executable, '-m', 'pylint', 'waves_gateway'])

        exit(code)


class PydocCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys, subprocess, os, shutil

        if os.path.exists("docs"):
            shutil.rmtree("docs")

        os.mkdir("docs")

        cwd = os.path.join(os.getcwd(), "docs")

        code = subprocess.call([sys.executable, '-m', 'pydoc', '-w', './../'], cwd=cwd)

        exit(code)


setup(
    name='waves_gateway',
    url='https://github.com/jansenmarc/WavesGatewayFramework',
    version='1.0.0',
    test_suite='nose.collector',
    tests_require=['nose'],
    install_requires=[
        'PyWaves>=0.7.9', 'python-doc-inherit>=0.3.0', 'simplejson>=3.11.1', 'requests>=2.9.1', 'base58>=0.2.5',
        'pymongo>=3.4.0', 'Flask>=0.12.2', 'gevent>=1.2.2'
    ],
    description='A framework to connect other cryptocurrencies to the Waves-Platform.',
    package_data={'waves_gateway': ['static/**/*', 'static/*']},
    license='MIT',
    long_description=open('README.md').read(),
    packages=find_packages(exclude=['waves_gateway.tests']),
    cmdclass={
        'coverage': CoverageCommand,
        'mypy': MyPyCommand,
        'lint': LintCommand,
        'pydoc': PydocCommand
    })