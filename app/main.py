from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

def validate_host(host: str):
    if not all(c.isalnum() or c in ('-', '.', '_') for c in host):
        raise ValueError('Invalid host name')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    output = safe_ping(host)
    return {"status": "completed", "output": output}