import os
import shutil
import time
from typing import List


class FilesystemClient:

    @staticmethod
    def remove_file_or_dir(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

    @staticmethod
    def delete_files_from_dir_older_then(dir_path, days=0, hours=0, minutes=0, seconds=0) -> List[str]:
        current_time = time.time()
        msg = []
        for filename in os.listdir(dir_path):
            full_path = "{}/{}".format(dir_path, filename)
            creation_time = os.path.getctime(full_path)
            age = current_time - creation_time
            old_age = (((days*24 + hours) * 60 + minutes) * 60) + seconds
            if age >= old_age:
                FilesystemClient.remove_file_or_dir(full_path)
                msg.append('{} removed'.format(full_path))
        return msg