from setuptools import setup

setup(
    name='ugapi',
    description='Ultimate-Guitar Tab API',
    url='http://github.com/doodoroma/ugapi',
    author='Adam Meszaros',
    author_email='doodoroma@gmail.com',
    license='MIT',
    packages=['ugapi'],
    install_requires=[
        'scrapy'
    ],
    zip_safe=False
)
