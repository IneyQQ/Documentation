from datetime import datetime
from subprocess import Popen
import os
import tempfile
from glob import glob


def get_date_with_file_format():
    return datetime.now().strftime("%F_%H-%M-%S")


def get_unix_basename(path):
    return os.path.basename(os.path.normpath(path))


def gzip_open(path):
    decompressed = tempfile.TemporaryFile()
    Popen(["gzip", "-d"], stdin=open(path), stdout=decompressed).wait()
    decompressed.flush()
    decompressed.seek(0)
    return decompressed


def get_last_modified_file_from_wildcard(wildcard):
    return max(glob(wildcard), key=os.path.getctime)
