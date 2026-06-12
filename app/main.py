from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        parts = shlex.split(command)
        subprocess.run(parts, check=True, capture_output=True, text=True, *args, **kwargs)

app = FastAPI()

def escape_shell_arg(arg):
    return shlex.quote(str(arg))

@app.get('/ping')
def ping(host: str):
    command = f'ping {escape_shell_arg(host)}'
    SafeSubprocess.run(command)
    return {'status': 'completed'}