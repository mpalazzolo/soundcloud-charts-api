from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='soundcloud-charts-api',
    url='https://github.com/mpalazzolo/soundcloud-charts-api',
    version='1.0.4',
    packages=['soundcloudcharts'],
    license='LICENSE.txt',
    author='Matt Palazzolo',
    author_email='mattpalazzolo@gmail.com',
    description='A python wrapper for the Soundcloud Chart API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'requests>=2.22.0',
        'bs4>=0.0.1'
    ],
)
