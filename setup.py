from setuptools import setup, find_packages

VERSION = '1.3.5' 
DESCRIPTION = 'RDS Group Generator'
LONG_DESCRIPTION = """RDS Group encoder & decoder made in Python 3.10 (you need 3.10 or up for this for its match use)
Source Code: https://flerken.zapto.org:1115/kuba/librds (also includes a better readme)"""

setup(
        name="librds", 
        version=VERSION,
        author="kuba201",
        author_email="kuba.pro010+librds@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        
        keywords=['radiodatasystem','rds'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Intended Audience :: Telecommunications Industry",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.10",
            "Development Status :: 4 - Beta"
        ]
)