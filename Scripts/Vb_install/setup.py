from setuptools import setup

setup(
    name='Vb_import',
    version='0.2',
    py_modules=['Vb_import'],
    install_requires=[
        'Click', 'Biomart'
    ],
    entry_points='''
        [console_scripts]
        Vb_import=Vb_import:search
    ''',
)