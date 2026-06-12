from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    args = ['ping', '-c', '1'] + shlex.split(host)  # Use shlex to safely split the command line arguments
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)