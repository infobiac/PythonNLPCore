__author__ = 'cjr2185'

from setuptools import setup, Command, find_packages

setup(
    name='PythonNLPCore',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/infobiac/PythonNLPCore',
    license='MIT',
    author='Columbia University',
    author_email='cjr2185@columbia.edu',
    description='NLP Core library for Python (With relational support)',
    cmdclass={},
    download_url='https://github.com/infobiac/PythonNLPCore/tarball/0.1',
    keywords=['nlp', 'ir'],
)
