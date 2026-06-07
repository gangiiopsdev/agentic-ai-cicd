from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __call__(self, host: str):
        # Validate the host input to ensure it does not contain malicious commands
        if '/' in host or '\' in host:
            raise ValueError('Invalid host input')
        args = shlex.split(f'ping {host}')
        subprocess.run(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_pinger = SafePing()
    try:
        safe_pinger(host)
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}