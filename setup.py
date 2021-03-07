from setuptools import setup, find_packages


def get_long_description(path):
    """Opens and fetches text of long descrition file."""
    with open(path, 'r') as f:
        text = f.read()
    return text


attrs = dict(
    name='date-time-event',
    version='0.0.1',
    packages=find_packages(),
    long_description=get_long_description('README.md'),
    description='A very simple package to trigger events at a specific DateTime.',
    long_description_content_type='text/markdown',
    author='Saad Mairaj',
    author_email='Saadmairaj@yahoo.in',
    url='https://github.com/Saadmairaj/date-time-event/',
    license='MIT',
    python_requires='>=3',
    keywords=[
        'python',
        'python3',
        'threading',
        'datetime-format',
        'date-event',
        'time-event'
    ],
    classifiers=[
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    project_urls={
        'Bug Reports': 'https://github.com/Saadmairaj/date-time-event/issues',
        'Source': 'https://github.com/Saadmairaj/date-time-event',
    },
    include_package_data=True,
)

setup(**attrs)