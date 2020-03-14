from setuptools import setup

setup(
    name='irispy',
    version='1.0',
    packages=['irispy', 'irispy.types', 'irispy.dispatcher'],
    url='https://github.com/zpodushkin/irispy',
    license='GPL-3.0',
    author='zpodushkin',
    description='Async and fast api wrapper for IrisCallback API',
    install_requires=['aiohttp', 'pydantic', 'loguru']
)
