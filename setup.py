import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='testFuncMN', ##name of repo enclosing folder (pip-package-demo)
    version='0.0.3',
    author='Mrinalini Nayak', ## your name
    author_email='mnayak20.mn@gmail.com', ## your email
    description='math functions i use a lot', ## description of package
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/meanieminnie/testFuncMN',# url to repo
    project_urls = {
        "Bug Tracker": "https://github.com/meanieminnie/testFuncMN/issues"
    }, ## url to issues page on your repo
    license='MIT',
    packages=['mathFunctions'], ## name of folder that holds the functions
    install_requires=[], ## names of packages required to run your functions
)