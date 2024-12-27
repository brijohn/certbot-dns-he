from setuptools import find_packages
from setuptools import setup


version = '1.0.0'

install_requires = [
    'setuptools',
    'requests',
    'certbot>=3.0.0',
]

setup(
    name='certbot-dns-he',
    version=version,
    description='Hurricane Electric DNS Authenticator plugin for Certbot (Using DDNS)',
    url='https://github.com/brijohn/certbot-dns-he',
    author='Brian Johnson',
    author_email='brijohn@gmail.com',
    license='MIT',
    python_requires='>=3.9',
    classifiers=[
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    keywords='certbot dns hurricane-electric dns-01 authenticator api ddns',

    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        'certbot.plugins': [
            'dns-he = certbot_dns_he.dns_he:Authenticator',
        ],
    }
)
