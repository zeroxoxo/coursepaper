from setuptools import setup

setup(
    name='Workflow',
    version='0.1',
    py_modules=['Workflow'],
    install_requires=[
        'Click', 'Biomart', 'Pandas'
    ],
    entry_points='''
        [console_scripts]
        Workflow=Workflow:Workflow
    ''',
)