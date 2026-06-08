from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        args = [shlex.quote(arg) for arg in args]
        full_command = command + ' '.join(args)
        return subprocess.run(full_command, shell=False, **kwargs)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if '@' not in host and len(host) <= 255:
        SafeSubprocess.run('ping', host)
    else:
        return {"error": "Invalid hostname"}
    return {"status": "completed"}