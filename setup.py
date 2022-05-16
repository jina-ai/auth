import sys

from setuptools import find_packages, setup

if sys.version_info < (3, 7, 0):
    raise OSError(f'Requires Python >=3.7, but yours is {sys.version}')

try:
    with open('README.md', encoding='utf8') as fp:
        _long_description = fp.read()
except FileNotFoundError:
    _long_description = ''

# package requirements
try:
    with open('requirements.txt', 'r') as f:
        _install_requires = f.readlines()
except FileNotFoundError:
    _install_requires = []

setup(
    name='jina-auth',
    packages=find_packages(),
    include_package_data=True,
    description='A CLI for you to login in to Jina Ecosystem',
    author='Jina AI',
    author_email='hello@jina.ai',
    license='Apache 2.0',
    url='https://github.com/jina-ai/auth',
    download_url='https://github.com/jina-ai/auth/tags',
    long_description=_long_description,
    long_description_content_type='text/markdown',
    zip_safe=False,
    setup_requires=['setuptools>=18.0', 'wheel'],
    install_requires=_install_requires,
    extras_require={
        'test': [
            'pytest',
            'pytest-timeout',
            'pytest-mock',
            'pytest-cov',
            'pytest-repeat',
            'pytest-reraise',
            'mock',
            'pytest-custom_exit_code',
            'black==22.3.0',
            'jina',
            'flake8',
            'isort',
        ],
    },
    entry_points={
        'console_scripts': [
            'jina-auth=auth.__main__:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Unix Shell',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Database :: Database Engines/Servers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Multimedia :: Video',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    project_urls={
        'Documentation': 'https://github.com/jina-ai/auth/',
        'Source': 'https://github.com/jina-ai/auth/',
        'Tracker': 'https://github.com/jina-ai/auth/issues',
    },
    keywords='jina auth login logout user',
)
