from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def ping(host: str):
        if not host or not host.strip():
            return False
        args = ['ping', *shlex.split(host)]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout,

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    if not host or not host.strip():
        return {"status": "failed", "message": "Invalid input"}
    try:
        response = SafePing.ping(host)
        return {"status": "completed", "output": response}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}