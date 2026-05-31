from setuptools import setup, find_packages

DESCRIPTION = (
    'Python library for interacting with the Patreon API. '
    'OAuth-centric for now.'
)

setup(
    name='patreon',
    version='0.5.1',
    description=DESCRIPTION,
    url='http://github.com/Patreon/patreon-python',
    author='Patreon',
    author_email='platform@patreon.com',
    license='Apache 2.0',
    packages=find_packages(
        exclude=['examples', 'examples.*', 'test', 'test.*']
    ),
    install_requires=[
        'requests',
        'six>=1.10.0',
    ],
    python_requires='>=3.9',
    extras_require={
        'test': [
        'pytest',
        'pytest-cov',
        'mock',
        ],
    },
    zip_safe=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ]
)
