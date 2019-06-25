from coreinterfaces.logs import Log


class FileLog(Log):
    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, obj):
        with open(self.file_path, 'a') as file:
            self._write_obj_to_file(file, obj)

    def write_iterable(self, iterable):
        with open(self.file_path, 'a') as file:
            for obj in iterable:
                self._write_obj_to_file(file, obj)

    def _write_obj_to_file(self, file, obj):
        file.write(str(obj))
        file.write('\n')

