from setuptools import setup


setup(
    name='alfred-coordinator',
    version='0.1.dev',
    license='ISC',
    description='Streams tasks from listener to workers.',
    url='https://github.com/alfredhq/alfred-coordinator',
    author='Alfred Developers',
    author_email='team@alfredhq.com',
    py_modules=['alfred_coordinator'],
    install_requires=[
        'PyYAML',
        'pyzmq',
    ],
    entry_points={
        'console_scripts': [
            'alfred-coordinator = alfred_coordinator:main',
        ],
    },
)
