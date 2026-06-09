from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    safe_hosts = ['8.8.8.8', '127.0.0.1']
    return host if host in safe_hosts else None
class SafeSubprocess:
    @staticmethod
def run(command, **kwargs):
        if isinstance(command, str):
            command = shlex.split(command)
        return subprocess.run(command, **kwargs)

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    safe_host = sanitize_host(host)
    if safe_host is None:
        return {"status": "error", "message": "Invalid host"}
    result = SafeSubprocess.run(['ping', safe_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}