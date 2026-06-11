from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    @staticmethod
def ping(host: str):
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    safe_ping = SafePing()
    return safe_ping.ping(shlex.quote(host))

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}