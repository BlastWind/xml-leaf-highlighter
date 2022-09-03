from setuptools import setup
setup(
    name='xml_leaf_highlighter',
    version='0.0.1',
    entry_points={
        'console_scripts': ['xlh = xml_leaf_highlighter.main:main']
    }, 
    packages=["xml_leaf_highlighter"],
    install_requires=["Pillow"]
)
