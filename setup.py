from setuptools import setup

setup(
    name='ImgCorrupter',
    version='1.0',
    packages=['ImgCorrupter'],
    author='Martico2432',
    author_email='',
    description='A Python  package to corrupt images with a lot of noise, use this if you want to destroy images.',
    url='https://github.com/Martico2432/ImageCorrupter',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[
        'tqdm',
        'random',
        'pillow'
    ],
)