from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run_command(command: str, *args, **kwargs):
        if not isinstance(command, list):
            command = shlex.split(command)
        return subprocess.run(command, *args, **kwargs)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    SafeSubprocess.run_command(f"ping", host)

    return {"status": "completed"}