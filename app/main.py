from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)