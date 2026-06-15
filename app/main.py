from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        try:
            return subprocess.run(shlex.split(command), *args, **kwargs)
        except subprocess.CalledProcessError as e:
            return e.output.decode('utf-8')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 255:
        return {"status": "failed", "error": "Invalid input"}
    command = f'ping -c 1 {host}'
    result = SafeSubprocess.run(command, capture_output=True, text=True)
    if isinstance(result, subprocess.CalledProcessError):
        return {"status": "failed", "error": str(result)}
    else:
        return {"status": "completed", "output": result.stdout}