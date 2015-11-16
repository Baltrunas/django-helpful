from setuptools import setup, find_packages

PACKAGE = "helpful"
NAME = "django-helpful"
DESCRIPTION = "Django helpful things"
AUTHOR = "Stanislav Baltrunas"
AUTHOR_EMAIL = "stanislav@baltrunas.ru"
URL = "https://github.com/Baltrunas/django-helpful"
VERSION = __import__(PACKAGE).__version__

setup(
	name=NAME,
	version=VERSION,
	description=DESCRIPTION,
	long_description=open('README.rst').read(),
	author=AUTHOR,
	author_email=AUTHOR_EMAIL,
	license="BSD",
	url=URL,
	packages=find_packages(exclude=["tests.*", "tests"]),
	# package_data=find_package_data(
			# PACKAGE,
			# only_in_packages=False
	  # ),
	classifiers=[
		"Development Status :: 3 - Alpha",
		"Environment :: Web Environment",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: BSD License",
		"Operating System :: OS Independent",
		"Programming Language :: Python",
		"Framework :: Django",
	],
	zip_safe=False,
)