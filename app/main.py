from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with shell=False
    if not host.isalnum():
        raise ValueError('Invalid host')
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    status = safe_ping(host)
    return {'status': 'completed', 'output': status}