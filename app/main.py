from fastapi import FastAPI
import subprocess
class SafeSubprocess:
    @staticmethod
def run_command(command, *args, **kwargs):
        args = [arg for arg in args if isinstance(arg, str)]
        safe_args = shlex.split(command)
        return subprocess.run(safe_args, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and args as a list
    safe_command = ['ping', host]
    return SafeSubprocess.run_command(safe_command, check=True)