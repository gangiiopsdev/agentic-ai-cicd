from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid host')
    args = ['ping', *shlex.split(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)