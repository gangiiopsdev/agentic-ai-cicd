from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        args = shlex.split(command)
        return subprocess.run(args, *args, **kwargs)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = f'ping {sanitized_host}'
    SafeSubprocess.run(command)
    return {"status": "completed"}

def sanitize_input(input_string):
    # Implement input sanitization logic here
    return ''.join(e for e in input_string if e.isalnum() or e in ('.', '-'))