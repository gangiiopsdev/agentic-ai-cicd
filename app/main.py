from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1', '::1']

    def ping(self, host: str):
        if host in self.allowed_hosts:
            args = ['ping'] + shlex.split(host)
            result = subprocess.run(args, capture_output=True, text=True)
            return result.stdout
        else:
            return 'Ping to non-localhost hosts is not allowed.'

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping_instance.ping(host)
    return {"status": "completed", "output": result}