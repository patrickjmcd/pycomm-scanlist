import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from pycomm_scanlist import Scanlist
from pycomm_scanlist.tag import Tag


def test_initialize():
    scan_list = Scanlist('192.168.1.11')
    assert isinstance(scan_list, Scanlist)
    assert scan_list.plc_ip_address == '192.168.1.11'

def test_addtag():
    scan_list = Scanlist('192.168.1.11')
    scan_list.add('test_tag_name')
    assert isinstance(scan_list.tags['test_tag_name'], Tag)
    assert len(scan_list.tags['test_tag_name'].evt_change._getfunctionlist()) > 0
    

