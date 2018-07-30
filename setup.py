import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pycomm-scanlist',
    version='0.1',
    author="Patrick McDonagh",
    author_email="patrickjmcd@gmail.com",
    url="https://github.com/patrickjmcd/pycomm-scanlist",
    packages=setuptools.find_packages(),
    license='GNU General Public License v3.0',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'pycomm'
    ]
)