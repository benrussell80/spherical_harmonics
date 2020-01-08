from setuptools import setup, find_packages

setup(
    name="spherical_harmonics",
    version="0.0.3",
    packages=find_packages(),
    entry_points={},
    python_requires='>=3.6',
    install_requires=[
        'bokeh',
        'Jinja2',
        'MarkupSafe',
        'numpy',
        'packaging',
        'Pillow',
        'pscript',
        'pyparsing',
        'python-dateutil',
        'PyYAML',
        'selenium',
        'six',
        'tornado',
        'urllib3'
    ],
    package_data={},
    author="Ben Russell",
    author_email="",
    description="",
    long_description="",
    keywords="",
    url="",
    project_urls={},
    classifiers=[]
)

# python3 setup.py sdist bdist_wheel
# python3 -m twine upload dist/*