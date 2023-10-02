import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = "0.0.0"

REPO_NAME = "textsummarizer"
AUTHOR_NAME = "aniketsaurav18"
SRC_REPO = "textsummarizer"
AURTHOR_EMAIL = "aniketsaurav18@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AURTHOR_EMAIL,
    description="Text Summarizer",
    long_description="Text Summarizer",
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{SRC_REPO}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
