from setuptools import setup, find_packages

setup(
    name='variegata',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'bs4',
        'Flask',
        'html5validator',
        'pycodestyle',
        'pydocstyle',
        'pylint',
        'pytest',
        'requests',
    ],
    python_requires='>=3.6',
)
