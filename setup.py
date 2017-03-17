from setuptools import setup, find_packages
# python setup.py register
# python setup.py sdist upload

setup(
	name="django-helpful",
	version="1.2.1",
	description="Django helpful things",
	long_description=open('README.rst').read(),
	author="Stanislav Baltrunas",
	author_email="stanislav@baltrunas.ru",
	license="BSD",
	url="https://github.com/Baltrunas/django-helpful",
	packages=find_packages(exclude=["tests.*", "tests"]),
	package_data={
		'templates' :['*'],
		'static' :['*'],
		'locale': ['*'],
		'docs': ['*'],
	},
	include_package_data=True,
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
