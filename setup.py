from setuptools import setup


setup(
    name='httpie-consul-discovery',
    description='Consul discovery plugin for httpie',
    long_description=open('README.md').read().strip(),
    version='0.0.1',
    author='Marcin Skalski',
    author_email='skalskimarcin33@gmail.com',
    license='Apache License 2.0',
    url='https://github.com/httpie/httpie-unixsocket',
    py_modules=['httpie_consul_discovery'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.transport.v1': [
            'httpie_http_consul_discovery = httpie_consul_discovery:HttpieConsulDiscoveryPluginHttp',
            'httpie_https_consul_discovery = httpie_consul_discovery:HttpieConsulDiscoveryPluginHttps'
        ]
    },
    install_requires=[
        'httpie>=3.0.2',
        'requests>=2.27.1'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3.9',
        'Environment :: Plugins',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)