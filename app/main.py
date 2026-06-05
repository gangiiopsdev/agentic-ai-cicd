from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run_command(command, *args, **kwargs):
        args = [arg for arg in args if isinstance(arg, str)]
        full_command = command.format(*args)
        safe_args = shlex.split(full_command)
        return subprocess.run(safe_args, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    command_parts = ['ping', shlex.quote(host)]
    return SafeSubprocess.run_command(*command_parts, check=True)