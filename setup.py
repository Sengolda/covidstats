from setuptools import setup


with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()


packages = [
"covidstats"
]

args = dict(
    name='covidtats',
    version='0.1.0',
    description='A Covid Statics tracker.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Sengolda/covidstats',
    author='Sengolda',
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=['aiohttp>=3.6,<3.8', 'requests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)

setup(**args)