import os, sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def get_root_dir():
    if hasattr(sys, 'real_prefix'):
        return sys.prefix
    else:
        return os.path.split(sys.prefix)[0]

setup(
    name='wonderland-engine',
    version='0.9',
    packages=['WhiteRabbit', 'WhiteRabbit.checks', 'Doorknob', 'CheshireCat',
              'CheshireCat.blueprints', 'CheshireCat.blueprints.checks',
              'CheshireCat.blueprints.teams'],
    scripts=['run_cheshire_cat.py', 'run_white_rabbit.py'],

    install_requires=[
        'Flask',
        'Jinja2',
        'Werkzeug',
        'redis',
        'configobj',
        'pymongo',
        'py-bcrypt',
        'Flask-Login',
        'parcon',
        'argparse'
    ],

    data_files=[
        (os.path.join(get_root_dir(), 'etc', 'wonderland-engine'), ['configspec.cfg', 'settings.cfg'])
    ],

    test_suite='nose.collector',
    tests_require='nose',
    url='http://smartboyathome.github.com/Wonderland-Engine/',
    license='AGPL',
    author='smartboyathome',
    author_email='smartboyathome@gmail.com',
    description='The Wonderland Cyber Defense Scoring Engine is a scoring engine for use in cyber defense competitions and practices. See the docs for more details.'
)