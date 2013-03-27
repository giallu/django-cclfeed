import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'django-cclfeed',
    version = '0.1',
    packages = ['cclfeed', 
                'cclfeed.management', 
                'cclfeed.management.commands'],
    include_package_data = True,
    license = 'MIT License',
    description = 'Create a RSS feed out of messages from CCL mailing list',
    long_description = README,
    url = 'http://github.com/giallu/django-cclfeed',
    author = 'Gianluca Sforna',
    author_email = 'giallu@gmail.com',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
