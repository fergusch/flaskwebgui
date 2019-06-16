from setuptools import setup, find_packages

#python setup.py bdist_wheel sdist
#cd dist 
#twine upload *


with open("README.md", "r") as fh:
    long_description = fh.read()


setup (
	name="flaskwebgui",
	version="0.0.7",
	description="Create desktop applications with Flask!",
	url="https://github.com/ClimenteA/flaskwebgui",
	author="Climente Alin",
	author_email="climente.alin@gmail.com",
	license='MIT',
	py_modules=["flaskwebgui"],
	install_requires=[
          'psutil',
		  'whichcraft',
      ],
	packages=find_packages(),
	long_description=long_description,
    long_description_content_type="text/markdown",
	package_dir={"":"src"}
)