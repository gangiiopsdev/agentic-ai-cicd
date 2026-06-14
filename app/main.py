from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def safe_run(command: str):
        args = shlex.split(command)
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout,

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        safe_host = shlex.quote(host)
        result = SafeSubprocess.safe_run(f'ping -c 1 {safe_host}')  # Limit the number of pings to prevent resource exhaustion
        return {"status": "completed", "output": result}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}