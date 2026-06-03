from fastapi import FastAPI
import subprocess
import shlex
class CommandExecutor:
    def __init__(self):
        self.command_map = {'ping': self.ping}

    def execute(self, command: str, host: str):
        parts = command.split()
        if parts[0] in self.command_map:
            return getattr(self, parts[0])(host)
        else:
            raise ValueError('Unknown command')

    def ping(self, host: str):
        try:
            output = subprocess.check_output(['ping', shlex.quote(host)], stderr=subprocess.STDOUT, timeout=5, shell=False)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}
class App:
    def __init__(self):
        self.executor = CommandExecutor()

    def ping_endpoint(self, command: str, host: str):
        try:
            return self.executor.execute(command, host)
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}
app = App()