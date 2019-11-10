from setuptools import setup

setup(
    name='VBSB',
    version='0.9d',
    py_modules=['VBSB'],
    install_requires=[
        'Click', 'Biomart', 'Pandas', 'Setuptools'
    ],
    entry_points='''
        [console_scripts]
        VBSB=VBSB:VBSB
    ''',
)
