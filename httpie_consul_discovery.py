from httpie.plugins import TransportPlugin
import consul_config
from consul_adapter import ConsulDiscoveryAdapter


class HttpieConsulDiscoveryPluginHttp(TransportPlugin):
    name = "Consul discovery plugin"

    prefix = "http+consul://"

    def get_adapter(self):
        return ConsulDiscoveryAdapter("http://", consul_config.CONSUL_ADDRESSES)

class HttpieConsulDiscoveryPluginHttps(TransportPlugin):
    name = "Consul discovery plugin"

    prefix = "htts+consul://"

    def get_adapter(self):
        return ConsulDiscoveryAdapter("https://", consul_config.CONSUL_ADDRESSES)