import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand


# ref: https://tox.readthedocs.org/en/latest/example/basic.html#integration-with-setuptools-distribute-test-commands
class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = ''

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        errno = tox.cmdline(args=shlex.split(self.tox_args))
        sys.exit(errno)


setup(
    name='datacheck',
    version='0.0.1',
    packages=['datacheck'],
    url='https://github.com/csdev/datacheck',
    license='MIT',
    author='Christopher Sang',
    description='data validation library',
    long_description='data validation library',

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
    ],

    tests_require=['tox'],
    cmdclass={'test': Tox},
)
