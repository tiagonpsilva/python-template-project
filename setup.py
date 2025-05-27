from setuptools import setup, find_packages

setup(
    name='python-template-project',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    author='Tiago N. P. Silva',
    description='Template de projeto Python com estrutura padr?o e boas pr?ticas.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tiagonpsilva/python-template-project',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
