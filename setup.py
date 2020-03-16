from setuptools import setup

setup(
    name='irispy',
    version='1.0.5',
    packages=['irispy', 'irispy.types', 'irispy.dispatcher', 'irispy.utils'],
    url='https://github.com/zpodushkin/irispy',
    license='GPL-3.0',
    author='zpodushkin',
    description='Async and fast api wrapper for IrisCallback API',
    install_requires=['aiohttp', 'pydantic', 'loguru', 'vbml']
)
