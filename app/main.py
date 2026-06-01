from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def validate_host(host):
        # Define a set of allowed hosts or use regex for validation
        allowed_hosts = {'example.com', 'test.com'}
        return host in allowed_hosts or re.match(r'^[a-zA-Z0-9.-]+$', host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if PingCommand.validate_host(host):
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 400