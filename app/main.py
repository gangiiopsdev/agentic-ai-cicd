from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def safe_call(command, *args, **kwargs):
        if isinstance(command, str) and shell=False not in kwargs:
            command = shlex.split(command)
        for i, arg in enumerate(args):
            args[i] = shlex.quote(arg)
        return subprocess.call(command, *args, **kwargs)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host and host.isalnum():  # Basic validation of the input
        SafeSubprocess.safe_call(f'ping', host)
    else:
        return {'status': 'invalid_host'}
    return {"status": "completed"}