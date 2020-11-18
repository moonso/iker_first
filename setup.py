# -*- coding: utf-8 -*-
import codecs
from setuptools import setup, find_packages


def parse_reqs(req_path='./requirements.txt'):
    """Recursively parse requirements from nested pip files."""
    install_requires = []
    with codecs.open(req_path, 'r') as handle:
        # remove comments and empty lines
        lines = (line.strip() for line in handle
                 if line.strip() and not line.startswith('#'))

        for line in lines:
            # check for nested requirements files
            if line.startswith('-r'):
                # recursively call this function
                install_requires += parse_reqs(req_path=line[3:])

            else:
                # add the line as a new requirement
                install_requires.append(line)

    return install_requires


setup(
    name='iker_first',
    version='0.1',
    url='https://github.com/moonso/iker_first',
    description='Simple text based game to learn math.',
    author='Måns Magnusson',
    author_email='monsun@me.com',
    packages=find_packages(exclude=['tests/', 'scripts/']),
    include_package_data=True,
    zip_safe=False,
    install_requires=parse_reqs(),
    entry_points=dict(
        console_scripts=[
            'spela = iker_first.__main__:cli',
        ]
    ),
    test_suite='tests',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries'
    ]
)
