import event

class Tag(object):

    evt_change = event.Event('Tag changed!')

    def __init__(self, tag_name):
        self.tag_name = tag_name
        self.last_value = None
        self.value = None
        self.value_changed = False

    def value_read(self, value):
        self.last_value = self.value
        self.value = value
        self.value_changed = (self.value != self.last_value)
        if self.value_changed:
            self.evt_change([self.tag_name, self.value, self.last_value])
    