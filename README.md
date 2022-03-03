# Httpie Consul discovery plugin

This plugin lets you use consul as service discovery when making request from `httpie`. While making request to your service, this plugin will extract actual IP and port of random service instance from Consul.

## Installation

Before installation, you need to update file `consul_config.py` with your environments and Consul addresses. Example config:

```
CONSUL_ADDRESSES = {
    "dev": "http://consul-dev.yourorg.com",
    "test": "http://consul-test.yourorg.com",
    "prod": "http://consul.yourorg.com",
}
```

Installation:

```bash
pip install -e .
```

## Example usage

To make request to `example-service` on environment `dev` for path `/status/info`, use:

```bash
http http+consul://example-service.dev/your/path
```

In order to trigger plugin, you need to use `http+consul://` or `https+consul://` protocol. Service name and environment is extracted from request host using pattern: `SERVICE_NAME.ENV`
