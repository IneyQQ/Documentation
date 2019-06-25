from coreinterfaces.model import Schedule
from coreinterfaces.job import Job
from datetime import datetime


class ScheduledTask:
    def set_job(self, job: Job):
        pass

    def get_job(self) -> Job:
        pass

    def set_schedule(self, schedule: Schedule):
        pass

    def get_schedule(self) -> Schedule:
        pass

    def get_next_run(self) -> datetime:
        pass

    def run(self):
        pass
