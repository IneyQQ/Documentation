from coreinterfaces.logs import Log


class LogContainer(Log):
    def __init__(self):
        self.logs = []

    def add_log(self, log: Log):
        self.logs.append(log)

    def write(self, obj):
        for log in self.logs:
            log.write(obj)

    def write_iterable(self, iterable):
        for log in self.logs:
            log.write_iterable(iterable)
