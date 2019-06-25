from coreinterfaces.logs import Log


class CLILog(Log):
    def write(self, obj):
        print(obj)

    def write_iterable(self, iterable):
        for obj in iterable:
            print(obj)
