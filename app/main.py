from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run with args and validation
    if not host or ' ' in host:
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_route(host: str):
    result = ping(host)
    return {"status": "completed", "output": result}