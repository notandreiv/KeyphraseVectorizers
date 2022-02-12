from distutils.util import convert_path

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

main_ns = {}
ver_path = convert_path('keyphrase_vectorizers/_version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

setuptools.setup(
    name='keyphrase-vectorizers',
    version=main_ns['__version__'],
    url='https://github.com/TimSchopf/KeyphraseVectorizers',
    license='BSD 3-Clause "New" or "Revised" License',
    author='Tim Schopf',
    author_email='tim.schopf@t-online.de.de',
    description='Set of vectorizers that extract keyphrases with part-of-speech patterns from a collection of text documents and convert them into a document-keyphrase matrix.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'numpy >= 1.18.5',
        'spacy >= 3.0.1',
        'nltk >= 3.6.1',
        'scikit-learn >= 1.0',
        'scipy>=1.7.3',
        'psutil>=5.8.0'
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires='>=3.7',
)
