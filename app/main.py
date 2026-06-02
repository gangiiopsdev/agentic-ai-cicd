from fastapi import FastAPI
import subprocess
import shlex

class CommandSanitizer:
    @staticmethod
def sanitize(command):
        return shlex.split(command)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid host name")
    command = CommandSanitizer.sanitize(f'ping {host}')
    subprocess.run(command, shell=False)
    return {"status": "completed"}