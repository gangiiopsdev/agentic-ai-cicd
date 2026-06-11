from fastapi import FastAPI
import subprocess
import shlex

def run_command(command):
    args = shlex.split(command)
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

class FastAPISecurity:
    def __init__(self):
        self.app = FastAPI()

    @app.get('/ping')
    def ping(self, host: str):
        command = f'ping {host}'
        output = run_command(command)
        return {'status': 'completed', 'output': output}