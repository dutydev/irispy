from setuptools import setup

setup(
    name='irispy',
    version='1.1.1',
    packages=['irispy', 'irispy.types', 'irispy.dispatcher', 'irispy.utils'],
    url='https://github.com/zpodushkin/irispy',
    download_url='https://github.com/zpodushkin/irispy/archive/1.1.tar.gz',
    license='GPL-3.0',
    author='zpodushkin',
    description='Async and fast api wrapper for IrisCallback API',
    install_requires=['aiohttp', 'pydantic', 'loguru', 'vbml']
)
