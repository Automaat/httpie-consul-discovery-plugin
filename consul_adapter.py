from random import choice
from httpie.adapters import HTTPieHTTPAdapter
from requests.models import PreparedRequest
import requests

class ConsulDiscoveryAdapter(HTTPieHTTPAdapter):
    def __init__(self, protocol, consul_envs, *args, **kwargs):
        self.protocol = protocol
        self.consul_envs = consul_envs
        super(ConsulDiscoveryAdapter, self).__init__(*args, **kwargs)

    def _strip_protocol(self, url):
        return url.split("://")[1]

    def _extract_url_components(self, url):
        host, path = url.split("/", 1)
        service_name, env = host.split(".")
        return service_name, env, path

    def _get_random_service_from_consul(self, service_name, env):
        consul_response = requests.get(
            f"{self.consul_envs[env]}/v1/catalog/service/{service_name}?stale"
        ).json()
        return choice(
            [f'{x["ServiceAddress"]}:{x["ServicePort"]}' for x in consul_response]
        )

    def send(self, request: PreparedRequest, stream, timeout, verify, cert, proxies):
        url = self._strip_protocol(request.url)
        service_name, env, path = self._extract_url_components(url)
        ip_from_consul = self._get_random_service_from_consul(service_name, env)

        request.url = f"{self.protocol}{ip_from_consul}/{path}"
        return super().send(request, stream, timeout, verify, cert, proxies)
