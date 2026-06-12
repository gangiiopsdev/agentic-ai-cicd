from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    return {'status': 'completed', 'output': safe_ping(host)}

def is_valid_host(host: str):
    allowed_hosts = ['example.com', 'test.example.com']  # Define a list of allowed hosts
    return host in allowed_hosts