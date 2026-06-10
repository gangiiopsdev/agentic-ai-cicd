from fastapi import FastAPI
import subprocess
import shlex

class SafeCommandExecutor:
    def __init__(self):
        self.whitelisted_commands = ['ping']

    def execute(self, command: str, *args):
        if command not in self.whitelisted_commands:
            raise ValueError(f"Invalid command: {command}")
        args = shlex.split(command)
        subprocess.call(args)

app = FastAPI()
safe_executor = SafeCommandExecutor()

def safe_ping(host: str):
    if not host.strip().isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        safe_executor.execute('ping', host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)