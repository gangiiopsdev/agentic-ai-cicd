from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        # Fixed implementation
        cmd = ['ping'] + shlex.split(host)
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    output = SafeSubprocess.ping(host)
    return {"status": "completed", "output": output}