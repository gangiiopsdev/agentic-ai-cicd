from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not valid_host(host):
        raise ValueError("Invalid host")
    args = ['ping', '-c', '1', host]
    subprocess.run(args, check=True)

@app.get('/ping')
def ping(host: str):
    return {"status": "completed", "message": safe_ping(host)}

def valid_host(host):
    # Add logic to validate the host parameter
    return True