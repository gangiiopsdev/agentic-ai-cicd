from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {"status": "completed", "output": response}