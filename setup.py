from setuptools import setup


def get_long_description():
    ''' returns the content of the README.md file as a string.
    '''
    from os import path

    this_directory = path.abspath(path.dirname(__file__))
        with open(path.join(this_directory, 'README.md'), mode='r', encoding='utf-8') as f:
            long_description = f.read()
    return long_description


def get_version():
    ''' returns the version number given in __init__.py as a string.
    '''
    import re

    with open("fasttrees/__init__.py", mode='r', encoding="utf8") as f:
        version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)
    return version


setup(
    name='fasttrees',
    version=get_version(),
    packages=['fasttrees'],
    url='https://github.com/dominiczy/fasttrees',
    license='MIT License',
    author='dominiczijlstra',
    author_email='dominiczijlstra@gmail.com',
    description='A fast and frugal tree classifier for sklearn',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    install_requires=[
                'numpy',
                'pandas',
                'sklearn',
                'logging'
          ]
)
