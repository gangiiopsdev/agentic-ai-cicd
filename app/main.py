from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def safe_run(command, *args, **kwargs):
        return subprocess.run(shlex.split(command), *args, **kwargs)
app = FastAPI()
def validate_host(host):
    if not host.isdigit() or len(host) > 15:
        raise ValueError("Invalid host")
@app.get("/ping")
def ping(host: str):