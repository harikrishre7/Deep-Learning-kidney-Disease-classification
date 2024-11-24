import setuptools

with open("README.md", "r" ,encoding= "utf-8") as f:    ## when creating a package it will read all the content present 
    long_description = f.read()                         ## README.md file and display it as description for that corresponding package.


__version__= "0.0.0"

REPO_NAME = "Deep-Learning-kidney-Disease-classification"
AUTHOR_USER_NAME = "harikrishre7"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = 'tphari18@gmail.com'

setuptools.setup(
    name = SRC_REPO,
    Version=__version__,
    author = AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description ="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type= "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir ={"": "src"},
    packages = setuptools.find_packages(where="src")
)