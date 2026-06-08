from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        # Fixed implementation
        cmd = ['ping'] + shlex.quote(host).split()
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping_safe(host: str):
    if not host or ' ' in host:
        raise ValueError("Invalid host parameter")
    output = SafeSubprocess.ping(host)
    return {"status": "completed", "output": output}