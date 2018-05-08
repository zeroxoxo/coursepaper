from setuptools import setup

setup(
    name='Workflow',
    version='0.9a',
    py_modules=['Workflow'],
    install_requires=[
        'Click', 'Biomart', 'Pandas', 'Setuptools'
    ],
    entry_points='''
        [console_scripts]
        Workflow=Workflow:Workflow
    ''',
)