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
    SafeSubprocess.run('ping', host)
    return {"status": "completed"}