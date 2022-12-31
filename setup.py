import re
from setuptools import setup

version = '2.0.1'


requirements = ['requests', 'beautifulsoup4']
    


readme = 'Search and get download links for any anime on Animepahe!'
with open('README.md', encoding="utf8") as f:
    readme = f.read()

setup(
    name='AnimepaheAPI',
    author='xenmods',
    author_email='ilumomin04@gmail.com',
    version=version,
    long_description=readme,
    url='https://github.com/xenmods/AnimepaheAPI',
    packages=['AnimepaheAPI'],
    license='GNU General Public License v3.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        "Natural Language :: English",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3.7',
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Build Tools",

    ],
    description='Search and get download links for any anime on Animepahe!',
    include_package_data=True,
    keywords=['anime', 'search', 'python', 'animepahe', 'download'],
    install_requires=requirements
)
