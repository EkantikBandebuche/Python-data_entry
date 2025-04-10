from setuptools import setup, find_packages

setup(
    name='flask-user-app',
    version='1.0.0',
    description='A simple Flask web app with SQLite database to collect user information.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==2.3.3',
        'Jinja2==3.1.3',
        'Werkzeug==2.3.7',
        'itsdangerous==2.1.2',
        'click==8.1.7',
        'MarkupSafe==2.1.5',
        'pytest==8.3.5'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Flask',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
