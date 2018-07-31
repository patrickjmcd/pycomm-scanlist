# Pycomm Scanlist

Python module for managing a list of tags being read from a Rockwell Automation PLC.

## Installation

### From PyPi

```Shell
pip install pycomm-scanlist
```

### From Source

```Shell
git clone https://github.com/patrickjmcd/pycomm-scanlist
cd pycomm-scanlist
python setup.py install
```

### *WORKAROUND FOR PYCOMM NOT BEING CORRECT VERSION*

If you are getting the following error:

```Shell
TypeError: open() got an unexpected keyword argument 'direct_connection'
```

You will need to install the [pycomm](https://github.com/ruscito/pycomm) module from source *AFTER* installing pycomm-scanlist

## Scanlist Class

The module implements a `Scanlist` class with a required parameter of IP Address. Optionally, a `plc_type` and a `change_handler` parameter can be passed to the class.

### `plc_type` parameter

Due to different implementations within `pycomm` for Micro800 PLCs, in order to read from a Micro800 PLC, the value of `plc_type` must be `"Micro800"`. The default value for `plc_type` is `"CLX"` for ControlLogix/CompactLogix PLCs.

### `change_handler` parameter

The `change_handler` should be a function with a required parameter `sender` and an optional parameter `eargs`. `sender` is a reference to the instance of `Tag` that has changed.

The default implementation of change_handler is:

```Python
def change_handler(sender):
    """Handle a tag value change."""
    print("{} changed from {} to {}".format(sender.tag_name, sender.last_value, sender.value))
```

### `Scanlist.add(tag_name)` function

`Scanlist.add` takes one parameter `tag_name` and adds it to the list of tags to scan.

### `Scanlist.remove(tag_name)` function

`Scanlist.add` takes one parameter `tag_name` and removes it from the list of tags to scan.

### `Scanlist.print_tag_names()` function

`Scanlist.print_tag_names()` prints all tag names currently in the list of tags to scan.

### `Scanlist.scan()` function

`Scanlist.scan()` polls all tags in the list of tags to scan and runs the `change_handler` function if the tag value has changed.

## Example

The following example creates two scanlists, one for the Micro800 PLC at 192.168.1.12 and another for the CLX PLC at 192.168.1.11. Each PLC has 4 tags in the scanlist.

```Python
import time
from pycomm_scanlist import Scanlist

def handle_tag_change(sender, eargs=None):
    """Handle a tag value change."""
    print("{} CHANGED FROM {} TO {}".format(sender.tag_name, sender.last_value, sender.value))

micro_scan_list = Scanlist("192.168.1.12", plc_type="Micro800", change_handler=handle_tag_change)
micro_scan_list.add("pond1Volume")
micro_scan_list.add("pond2Volume")
micro_scan_list.add("pond3Volume")
micro_scan_list.add("pond4Volume")

clx_scan_list = Scanlist("192.168.1.11", change_handler=handle_tag_change)
clx_scan_list.add("DH_Fluid_Level")
clx_scan_list.add("DH_IntakePressure")
clx_scan_list.add("DH_IntakeTemperature")
clx_scan_list.add("DH_MaxIntakePressure_Forever")

micro_scan_list.print_tag_names()
clx_scan_list.print_tag_names()

while True:
    micro_scan_list.scan()
    clx_scan_list.scan()
    time.sleep(5)

```

## TODO

- Add tests to increase coverage.
- Per-tag handlers?
- ~~PyPi package~~
- Fix broken pycomm package

## Contributors

- Patrick McDonagh - [@patrickjmcd](http://github.com/patrickjmcd) - Owner

## Special Thanks

Thanks to [@ruscito](https://github.com/ruscito) for his great work on the [pycomm](https://github.com/ruscito/pycomm) package.