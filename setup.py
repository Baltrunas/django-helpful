from setuptools import setup, find_packages
# python setup.py register
# python setup.py sdist upload
# python setup.py sdist bdist_wheel
# twine upload dist/*.whl

# python3 -m pip install --user --upgrade setuptools wheel
# python3 setup.py sdist bdist_wheel
# python3 -m twine upload --repository helpful dist/*

setup(
	name="django-helpful",
	version="1.5.8",
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
	install_requires=[],
	python_requires='>=2.6, <4',
	classifiers=[
		"Development Status :: 4 - Beta",
		"Environment :: Web Environment",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: BSD License",
		"Operating System :: OS Independent",
		"Programming Language :: Python",
		"Framework :: Django",
	],
	zip_safe=False,
)
