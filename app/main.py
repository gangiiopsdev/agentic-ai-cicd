from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host not allowed')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    args = ['ping', '-c', '1'] + shlex.split(host)
    output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
    return {"status": "completed", "output": output.decode()}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}