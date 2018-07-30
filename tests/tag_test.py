import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from pycomm_scanlist.tag import Tag

def test_tag_add():
    name = 'test_tag_name'
    tag = Tag(name)
    assert isinstance(tag, Tag)
    assert tag.tag_name == name

def test_value_changed():
    tag = Tag('test_tag_name')

    assert tag.value == None
    assert tag.last_value == None

    tag.value_read(100.0)
    assert tag.value == 100.0
    assert tag.last_value == None

    tag.value_read(True)
    assert tag.value == True
    assert tag.last_value == 100.0


VALUE_CHANGED = False
def handler(source, eargs):
    global VALUE_CHANGED
    VALUE_CHANGED = eargs

def test_handler():
    tag = Tag('test_tag_name')
    tag.evt_change += handler

    tag.value_read(100.0)
    print(VALUE_CHANGED)
    assert VALUE_CHANGED == ['test_tag_name', 100.0, None]
