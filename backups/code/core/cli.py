from subprocess import list2cmdline
from subprocess import Popen
from typing import List
from core.logs import LogContainer


class CLI(Popen):
    logs = LogContainer()

    def __init__(self, args, **options):
        super().__init__(args, **options)
        CLI.logs.write(list2cmdline(args))

    @staticmethod
    def sshpass(args: List[str], password: str) -> List[str]:
        return ["sshpass", "-p", password] + args

    @staticmethod
    def format_popen(args: List[str], **options) -> str:
        addition = []
        if "stdout" in options and hasattr(options["stdout"], 'name'):
            addition.append(">")
            addition.append(options["stdout"].name)
        elif "stdin" in options and hasattr(options["stdin"], 'name'):
            addition.append("<")
            addition.append(options["stdin"])
        elif "stderr" in options and hasattr(options["stderr"], 'name'):
            addition.append("2>")
            addition.append(options["stderr"])
        cmd = list2cmdline(args + addition)
        return cmd

    @staticmethod
    def popen_with_sshpass(args, password, **options):
        return CLI(CLI.sshpass(args, password), **options)
