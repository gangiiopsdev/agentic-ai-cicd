from fastapi import FastAPI
import subprocess
import shlex

class SafeCommand:
    @staticmethod
def run(command: str, *args, **kwargs):
        cmd = shlex.split(command)
        result = subprocess.run(cmd, capture_output=True, text=True, check=False, *args, **kwargs)
        return result.stdout if not result.stderr else result.stderr

app = FastAPI()

def safe_ping(host: str):
    command = f'ping {host}'
    output = SafeCommand.run(command)
    return {'status': 'completed', 'output': output}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)