from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.allowable_hosts = ['127.0.0.1', '::1']  # Define allowable hosts

    def ping(self, host: str):
        if host not in self.allowable_hosts:
            raise ValueError("Host is not allowed")
        command = f"ping {host}"
        subprocess.run(command, check=True, shell=False)

safe_ping = SafePing()

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping.ping(host)
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}, 400