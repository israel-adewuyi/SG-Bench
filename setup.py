from setuptools import setup, find_packages

setup(
    name="sgbench_toolkit",
    version="0.1.1",
    description="SG-Bench toolkit",
    author="ZenithX",
    author_email="waltersumbon@gmail.com",
    url="https://github.com/EasyJailbreak/EasyJailbreak",
    packages=find_packages() + ['datasets', 'test'],  # Treat as packages even without __init__.py
    include_package_data=True,
    package_data={
        '': ['*.json', '*.txt', '*.yaml', '*.yml'],
        'datasets': ['**/*'],  # Include everything in datasets
        'test': ['**/*'],      # Include everything in test
    },
    install_requires=[
        'transformers>=4.34.0',
        'protobuf',
        'sentencepiece',
        'datasets',
        'torch>=2.0',
        'openai>=1.0.0',
        'numpy',
        'pandas',
        'accelerate',
        'fschat',
        'jsonlines',
        'einops',
        'nltk',
        'transformers_stream_generator',
    ],
    python_requires=">=3.9",
    keywords=['jailbreak', 
              'llm security', 
              'llm safety benchmark',
              'large language model',
              'jailbreak framework',
              'jailbreak prompt',
              'discrete optimization'
             ],
    license='GNU General Public License v3.0',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3"
    ]
)
