from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def call(command: str):
        args = shlex.split(command)
        subprocess.call(args)

app = FastAPI()

@app.get("/ping")
def ping(host: str):     
    safe_host = host.replace(';', ' ;').replace('&', ' &')
    command = f"ping {safe_host}"
    SafeSubprocess.call(command)
    return {"status": "completed"}