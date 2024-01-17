from setuptools import setup, find_packages

setup(
    name='routemin', 
    version='0.1.2', 
    author='elmomuds',
    description='Shortest Route Search App',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'networkx',  
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
