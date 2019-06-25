from coreinterfaces.info import Info


class ListInfo(Info):
    def __init__(self):
        self.info = []

    def add(self, info):
        info_str = info.__repr__()
        if len(info_str) != 0:
            self.info.append(info_str)

    def clear(self):
        self.info.clear()

    def get(self):
        return "\n".join(self.info)
