from fastapi import FastAPI
import subprocess
class CommandExecutor:
    def __init__(self, command: str):
        self.command = command

    def execute(self, *args):
        try:
            result = subprocess.run([self.command] + [arg for arg in args if isinstance(arg, str)], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}

app = FastAPI()
def ping(host: str):
    executor = CommandExecutor('ping')
    # Sanitize input to prevent command injection
    return executor.execute(host)