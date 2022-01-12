import string
import tarfile
import sys
BZ2_AAVALIABLE = True
try:
    import bz2
except ImportError:
    BZ2_AAVALIABLE = False

UNTRUSTED_PREFIXES = tuple(['/','\\']+ [c+ ':' for c in string.ascii_letters])
def untar(archive):
    tar = None
    try:
        tar =  tarfile.open(archive)
        for mem in tar.getmembers():
            if mem.name.startswith(UNTRUSTED_PREFIXES):
                print('untrusted prefixes, ignoring ',mem.name)
            elif '..' in mem.name:
                print("suspectpath,ignoring",mem.name)
            else:
                tar.extract(mem)
                print('unpacked' , mem.name)
    except (tarfile.TarError, EnvironmentError) as err:
        error(err)
    finally:
        if tar is not None:
            tar.close()
            
def error(message, exit_status =1):
    print(message)
    sys.exit(exit_status)
