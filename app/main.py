from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Consider using a whitelist of allowed hosts or more robust input validation
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    response = safe_ping(host)
    return {"status": "completed", "output": response}