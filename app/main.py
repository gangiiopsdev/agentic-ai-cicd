from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def call(command, *args, **kwargs):
        args = [arg for arg in args]
        if isinstance(command, str):
            command = shlex.split(command)
        return subprocess.call(command, *args, **kwargs)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_host = shlex.quote(host)
    command = ['ping', safe_host]
    SafeSubprocess.call(command)

    return {"status": "completed"}