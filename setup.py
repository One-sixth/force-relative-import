from setuptools import setup

ver_str = '0.0.1.post1'

long_description = open('README.md', 'r', encoding='utf8').read()

setup(
    name='force-relative-import',
    version=ver_str,
    description='Allow users to bypass Python relative import restrictions.',
    author='onesixth',
    author_email='noexist@noexist.noexist',
    url='https://github.com/One-sixth/force-relative-import',
    install_requires=[],
    entry_points={'console_scripts': []},
    packages=['force_relative_import'],
    package_data={},
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
