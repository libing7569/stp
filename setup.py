from setuptools import setup, find_packages

setup(
    name = 'STP-LB',
    version = '0.1.dev0',
    description = 'simple tasks platform',
    author = 'libing',
    author_email = 'libing7569@hotmail.com',
    packages = find_packages('.'),
    package_data = {
        '': ['stserver'],
        'stp': ['conf/*.yaml', 'conf/*.conf']
    },
    url = 'https://github.com/libing7569/stp',
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
