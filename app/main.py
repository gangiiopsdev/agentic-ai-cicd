from fastapi import FastAPI
import subprocess
import shlex

def execute_ping(host):
    # Safe implementation using shlex.quote
    command = ['ping', shlex.quote(host)]
    subprocess.run(command)

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Add additional validation or use a whitelist for 'host'
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    execute_ping(host)
    return {"status": "completed"}