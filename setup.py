from setuptools import setup

try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except (Exception, FileNotFoundError):
    with open("README.md", "r") as f:
        long_description = f.read()

setup(
    name='irispy',
    version='1.2',
    packages=['irispy', 'irispy.types', 'irispy.dispatcher', 'irispy.utils'],
    url='https://github.com/zpodushkin/irispy',
    download_url='https://github.com/zpodushkin/irispy/archive/1.2.tar.gz',
    license='GPL-3.0',
    author='zpodushkin',
    description='Async and fast api wrapper for IrisCallback API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    install_requires=['aiohttp', 'pydantic', 'loguru', 'vbml', 'vkbottle']
)
