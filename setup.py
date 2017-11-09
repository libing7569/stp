from setuptools import setup, find_packages

setup(
    name = 'STP',
    version = '0.1-dev',
    description = 'simple tasks system',
    author = 'libing',
    packages = find_packages('.'),
    package_data = {
        '': ['stserver'],
        'stp': ['conf/*.yaml', 'conf/*.conf']
    },
    include_package_data=True,
    install_requires = [
        'setuptools>=36.6.0',
        'prompt_toolkit>=1.0.15',
        'psutil>=5.4.0',
        'Flask>=0.12.2',
        'Flask_RESTful>=0.3.6',
        'PyYAML>=3.12',
        'thrift>=0.10.0'
    ],
    scripts = ['stserver']
)
