from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ['example.com', 'test.example.com']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host not allowed'}
    args = ['ping', host]
    result = subprocess.run(shlex.split(' '.join(args)), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)