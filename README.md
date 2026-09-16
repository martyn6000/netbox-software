# NetBox Software Plugin

NetBox plugin for netbox-software.


* Free software: Apache-2.0
* Documentation: https://martyn6000.github.io/netbox-software/


## Features

- Track software License Types (name, description, color) for categorizing licenses
- Track Software Licenses (manufacturer, license name, friendly name, SKU, per-license cost, license type)
- REST API endpoints for programmatic access
- GraphQL support for flexible data queries
- Full change logging and journaling support
- Integration with NetBox's permission system
- Global search integration for finding license objects
- Comprehensive filtering and table views

## Screenshots

<!-- Add screenshots or GIFs demonstrating your plugin's functionality here -->
_Screenshots will be added as features are developed._

## Compatibility

This plugin requires **NetBox 4.3** or later.

| NetBox Version | Plugin Version |
|----------------|----------------|
|     4.3+       |      1.0       |

For more detailed compatibility information, see [COMPATIBILITY.md](COMPATIBILITY.md).

## Dependencies

This plugin requires:
- NetBox 4.3 or later
- Python 3.10 or later

No additional Python packages are required beyond NetBox's core dependencies.

## REST API

This plugin provides REST API endpoints for managing software license resources:

- `/api/plugins/netbox_software/license-types/` - List and create License Type objects
- `/api/plugins/netbox_software/software-licenses/` - List and create Software License objects


## GraphQL

This plugin provides GraphQL support for querying netbox-software resources through NetBox's GraphQL API.


## Installing

For adding to a NetBox Docker setup see
[the general instructions for using netbox-docker with plugins](https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins).

While this is still in development and not yet on pypi you can install with pip:

```bash
pip install git+https://github.com/martyn6000/netbox-software
```

or by adding to your `local_requirements.txt` or `plugin_requirements.txt` (netbox-docker):

```bash
git+https://github.com/martyn6000/netbox-software
```

Enable the plugin in `/opt/netbox/netbox/netbox/configuration.py`,
 or if you use netbox-docker, your `/configuration/plugins.py` file :

```python
PLUGINS = [
    'netbox_software'
]

PLUGINS_CONFIG = {
    "netbox_software": {},
}
```

## Configuration

This plugin does not require any additional configuration by default. Optional configuration parameters can be added to `PLUGINS_CONFIG` in your NetBox configuration file as needed.

## Usage

For detailed usage instructions, please refer to the [documentation](https://martyn6000.github.io/netbox-software/).

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Reporting Bugs

Please report bugs by opening an issue on our [GitHub Issues](https://github.com/martyn6000/netbox-software/issues) page. When reporting bugs, please include:

- NetBox version
- Plugin version
- Python version
- Steps to reproduce
- Expected behavior
- Actual behavior

### Feature Requests

Feature requests can be submitted as [GitHub Issues](https://github.com/martyn6000/netbox-software/issues) with the "enhancement" label.

## Support

- **Documentation**: https://martyn6000.github.io/netbox-software/
- **Issues**: https://github.com/martyn6000/netbox-software/issues
- **Discussions**: https://github.com/martyn6000/netbox-software/discussions
- **NetBox Community Slack**: [netdev-community.slack.com](https://netdev.chat/)

## Credits

Based on the NetBox plugin tutorial:

- [demo repository](https://github.com/netbox-community/netbox-plugin-demo)
- [tutorial](https://github.com/netbox-community/netbox-plugin-tutorial)

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [`netbox-community/cookiecutter-netbox-plugin`](https://github.com/netbox-community/cookiecutter-netbox-plugin) project template.
