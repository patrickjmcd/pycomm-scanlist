"""PLC data."""
import time
from pycomm.ab_comm.clx import Driver as ClxDriver
from pycomm.cip.cip_base import CommError, DataError

TAG_DATAERROR_SLEEPTIME = 5

def read_tag(addr, tag, plc_type="CLX"):
    """Read a tag from the PLC."""
    direct = plc_type == "Micro800"
    addr = str(addr)
    c = ClxDriver()
    try:
        if c.open(addr, direct_connection=direct):
            try:
                if type(tag) == type([]):
                    read_values = []
                    for t in tag:
                        read_values.append(c.read_tag(t))
                    return read_values
                else:
                    return c.read_tag(tag)
                return v
            except DataError as e:
                c.close()
                time.sleep(TAG_DATAERROR_SLEEPTIME)
                print("Data Error during readTag({}, {}, plc_type='{}'): {}".format(addr, tag, plc_type, e))
        else:
            raise DataError("no data")

    except CommError:
        # err = c.get_status()
        c.close()
        print("Could not connect during readTag({}, {})".format(addr, tag))
        # print err
    except AttributeError as e:
        c.close()
        print("AttributeError during readTag({}, {}): \n{}".format(addr, tag, e))
    c.close()

def write_tag(addr, tag, val, plc_type="CLX"):
    """Write a tag value to the PLC."""
    direct = plc_type == "Micro800"
    clx = ClxDriver()
    if clx.open(addr, direct_connection=direct):
        try:
            prevval = clx.read_tag(tag)
            if direct:
                time.sleep(1)
            write_result = clx.write_tag(tag, val, prevval[1])
            return write_result
        except Exception:
            print("Error during writeTag({}, {}, {})".format(addr, tag, val))
            err = clx.get_status()
            clx.close()
            print(err)
            return False
        clx.close()
    return False
