# PyGuru

A Python wrapper for the [LabGuru REST API](https://my.labguru.com/api-docs/index.html).

## Authentication and Configuration
PyGuru supports both username/password combo or using an already existing token.

If you want to use a pre-existing token, supply it to PyGuru via the `PYGURU_TOKEN` environment variable.  
Otherwise, you can supply the username and password to PyGuru in the ways described above, and they will be checked for in that order.


PyGuru also allows you to configure the following:
- Host - the base URL of the API, defaults to `my.labguru.com`.
- Account - account id, default to `None` for the basic usage of the API against a default account, but neccessary when you have multiple accounts (e.g., a testing account).
- Version - via the `version` constructor argument, defaults to `v1`.

PyGuru will try to configure these settings in the following order :
1. Constructor parameters:
```python
pyguru = PyGuru(
    username='usr',
    password='pwd',
    host='host.labguru.com', # Optional
    account_id=123456 # Optional
)
```
2. Environment Variables, via the following:
```shell
PYGURU_USERNAME
PYGURU_PASSWORD
PYGURU_HOST # Optional
PYGUURU_ACCOUNT_ID # Optional
```
3. Config file - located in `~/.pyguru/credentials` with the following keys:
```shell
[default]
username = ...
password = ...
host = ... # Optional
account = ... # Optional
```
If you choose to use a config file, you can also specify different profile names above each configuration and then simply passing the profile name to PyGuru like so:
```python
pyguru = PyGuru(profile='validation')
```
Please note that using a config file means your credentials are stored in plaintext at rest, which is not recommended.

## Endpoints
Currently not all endpoints are implemented, but they will be.
All implemented endpoints are registers undered the `PyGuru` object.

You can create your own endpoint class and register by extending the base endpoint class:
```python
from pyguru.base_labguru_endpoint import BaseLabguruEndpoint
from pyguru import PyGuru

class CustomEndpoint(BaseLabguruEndpoint):

    def __init__(self, adapter) -> None:
        super().__init__(adapter, 'custom')

pyguru = PyGuru()
pyguru.register_endpoint_cls('custom_endpoint', CustomEndpoint)
```

A useful feature of PyGuru is creating your own generic biocollections endpoint class in order to simplify working against the API.

Assume for example you have a generic collections to manage your company's bank of dragons, you create your own custom endpoint and register it:
```python
from pyguru.endpoints import BiocollectionsEndpoint
from pyguru.pyguru import PyGuru
class DragonsBankEndpoint(BiocollectionsEndpoint):

    def __init__(self, adapter) -> None:
        super().__init__(adapter, biocollection='dragons bank')

pyguru = PyGuru()
pyguru.register_endpoint_cls('dragons_bank', DragonsBankEndpoint)
dragons = pyguru.dragons_bank.get()
```

## Plugins
PyGuru offers a way to write your own plugins for commonly used methods involving the API which are not neccessarily officially supported by the API.
Each endpoint allows you to register a plugin function so it can be called directly from the endpoint, for example:
```python
from pyguru.plugins.elements import export_spreadjs_table
from pyguru.pyguru import PyGuru

element_id = 123
pyguru = PyGuru(profile='test')
pyguru.elements.register_plugin(export_spreadjs_table)
pyguru.elements.export_spreadjs_table(element_id)
```
In this example, the endpoint is required to be the first parameter of the plugin function so that the method binding will work. If you write your plugin this way, you can still call it without binding, e.g.:
```python
from pyguru.plugins.elements import export_spreadjs_table
from pyguru.pyguru import PyGuru

element_id = 123
pyguru = PyGuru(profile='test')
export_spreadjs_table(pyguru.elements, element_id)
```

## Disclaimer
This software is not affiliated, associated, authorized or endorsed by LabGuru.