from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_command(command):
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return result.stdout

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = ["ping", host]
    output = run_command(command)
    return {"status": "completed", "output": output}