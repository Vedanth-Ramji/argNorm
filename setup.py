from setuptools import setup

DESCRIPTION = """
Normalize antibiotic resistance genes (ARGs) results by using the ARO ontology (developed by CARD).
""".strip()

exec(compile(open('argnorm/argnorm_version.py').read(),
             'argnorm/argnorm_version.py', 'exec'))

setup(
    name='argnorm',
    version=__version__,  # noqa: F821
    author='ArgNorm Developers',
    author_email='luispedro@big-data-biology.org',
    url="https://github.com/BigDataBiology/argNorm",
    license='MIT',
    description=DESCRIPTION,
    packages=['argnorm', 'argnorm.data'],
    include_package_data=True,
    package_dir={'argnorm': 'argnorm' },
    package_data={'argnorm': [
        'data/aro.obo',
        'data/*.tsv',
        'data/manual_curation/*.tsv'
        ]},
    install_requires=open("./requirements.txt", "r").read().splitlines(),
    long_description=open("./README.md", "r").read(),
    long_description_content_type='text/markdown',
    entry_points={
        "console_scripts": [
            "argnorm=argnorm.cli:main"
        ]
    },
    zip_safe=False,
    classifiers=[
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English"
    ],
)
