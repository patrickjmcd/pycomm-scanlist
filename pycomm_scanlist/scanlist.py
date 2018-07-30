"""Scanlist class definition."""
from tag import Tag
from plc import read_tag

def change_handler(sender):
    """Handle a tag value change."""
    print("{} changed from {} to {}".format(sender.tag_name, sender.last_value, sender.value))

class Scanlist(object):
    """Scanlist of tags to evaluate and react to."""
    
    def __init__(self, plc_ip_address, plc_type="CLX", change_handler=change_handler):
        """Initialize the Scanlist"""
        self.plc_ip_address = plc_ip_address
        self.plc_type = plc_type
        self.tags = {}
        self.change_handler = change_handler

    def add(self, tag_name):
        """Add a tag to the scan list."""
        self.tags[tag_name] = Tag(tag_name)
        self.tags[tag_name].evt_change += self.change_handler

    def remove(self, tag_name):
        """Remove a tag from the scan list."""
        del self.tags[tag_name]

    def print_tag_names(self):
        """Print all tag names in the scan list."""
        print("----------")
        print("Tags for {}".format(self.plc_ip_address))
        print("----------")
        for tag in self.tags.keys():
            print(self.tags[tag].tag_name)
        print("~~~~~~~~~~")

    def scan(self):
        """Scan the tag list and run the change_handler function if the value has changed."""
        tag_name_list = self.tags.keys()
        values = read_tag(self.plc_ip_address, tag_name_list, plc_type=self.plc_type)
        for i in range(0, len(tag_name_list)):
            tag = self.tags[tag_name_list[i]]
            if len(values[i]) > 1:
                tag.value_read(values[i][0])

    
