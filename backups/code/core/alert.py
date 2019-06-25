from coreinterfaces.alert import Alert


class AlertContainer(Alert):
    def __init__(self):
        self.alerts = []

    def add_alert(self, alert):
        self.alerts.append(alert)

    def alert(self, theme, message):
        for alert in self.alerts:
            alert.alert(theme, message)
