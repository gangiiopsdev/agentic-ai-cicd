from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def call(command, *args, **kwargs):
        if isinstance(command, str):
            command = shlex.split(command)
        return subprocess.call(command, *args, **kwargs)

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('.', '-', '_'))

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    SafeSubprocess.call(["ping", sanitized_host])
    return {"status": "completed"}