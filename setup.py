from setuptools import setup, find_packages

setup(
    name='py-gfm',
    version='0.1.2',
    description='An implementation of Github-Flavored Markdown written as an extension to the Python Markdown library.',
    author='Dart Team',
    author_email='misc@dartlang.org',
    url='https://github.com/dart-lang/py-gfm',
    download_url='https://github.com/dart-lang/py-gfm/tarball/0.1.2',
    packages=find_packages(),
    include_package_data = True,
    install_requires = ['setuptools', 'markdown'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
