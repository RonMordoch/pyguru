# PyGuru



## Endpoints

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