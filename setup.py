from setuptools import setup

setup(
    name='ugapi',
    version='0.1',
    description='Ultimate-Guitar Tab API',
    url='http://github.com/doodoroma/ugapi',
    download_url='https://github.com/doodoroma/ugapi/archive/0.1.0.tar.gz',
    author='Adam Meszaros',
    author_email='doodoroma@gmail.com',
    license='MIT',
    packages=['ugapi'],
    install_requires=[
        'scrapy'
    ],
    zip_safe=False
)
