from setuptools import setup

ver_str = '0.0.1'

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
)
