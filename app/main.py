from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run_command(command: str, *args, **kwargs) -> int:
        args = shlex.split(command)
        return subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, *args, **kwargs).returncode

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    command = f'ping {{}}'.format(shlex.quote(host))
    result = SafeSubprocess.run_command(command)
    if result == 0:
        return {"status": "completed"}
    else:
        return {"status": "failed", "error": "Ping failed"}