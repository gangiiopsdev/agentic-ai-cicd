from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        return "Invalid host"
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'stdout': result.stdout, 'stderr': result.stderr}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)