from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def ping(host: str):
        if not host or not host.strip():
            return False
        args = ['ping', *shlex.split(host)]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout,

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    response = SafePing.ping(host)
    if response:
        return {"status": "completed", "output": response}
    else:
        return {"status": "failed"}