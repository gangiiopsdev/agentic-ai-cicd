from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run_command(command):
        args = shlex.split(command)
        subprocess.call(args)

app = FastAPI()

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    command = f"ping {host}"
    SafeSubprocess.run_command(command)

    return {"status": "completed"}