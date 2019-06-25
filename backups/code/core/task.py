from croniter import croniter
from core.logs import LogContainer
from core.alert import AlertContainer
from datetime import datetime
from heapq import heappop, heappush
import traceback
from time import sleep
from coreinterfaces.job import Job
from coreinterfaces import scheduledtask
from coreinterfaces import scheduledtaskmanager
from coreinterfaces.model import Schedule


class ScheduledTask(scheduledtask.ScheduledTask):

    def __init__(self, job: Job, schedule: Schedule):
        self.job = job
        self.schedule = schedule

    def set_job(self, job: Job):
        self.job = job

    def get_job(self) -> Job:
        return self.job

    def set_schedule(self, schedule: Schedule):
        self.schedule = Schedule

    def get_schedule(self) -> Schedule:
        return self.schedule

    def get_next_run(self) -> datetime:
        return croniter(self.schedule.get_schedule(), self.schedule.get_last_run()).get_next(datetime)

    def run(self):
        try:
            self.job.do()
        finally:
            self.schedule.set_last_run(datetime.now())

    def __lt__(self, other):
        return self.get_next_run() < other.get_next_run()


class ScheduledTaskManager(scheduledtaskmanager.ScheduledTaskManager):

    def __init__(self, logs=LogContainer(), error_logs=LogContainer(), alerts=AlertContainer()):
        self.logs = logs
        self.error_logs = error_logs
        self.alerts = alerts
        self.tasks = []

    def add_scheduled_task(self, scheduled_task: ScheduledTask):
        heappush(self.tasks, scheduled_task)

    def run_next_task(self):
        task = heappop(self.tasks)
        now_time = datetime.now()
        run_time = task.get_next_run()
        wait_delta = run_time - now_time
        wait_seconds = wait_delta.total_seconds()
        if wait_seconds > 0:
            msg = "Waiting to {}".format(run_time)
            self.logs.write(msg)
            self.alerts.alert("Task Manager waiting", msg)
            sleep(wait_seconds)
        try:
            task.run()
        except:
            self.logs.write(task.job.get_info().get())
            task.job.get_info().clear()
            trace = traceback.format_exc()
            self.error_logs.write_iterable([task, trace])
            self.alerts.alert("ERROR at task: " + str(task), traceback.format_exc())
        else:
            self.logs.write(task.job.get_info().get())
            task.job.get_info().clear()
        heappush(self.tasks, task)
