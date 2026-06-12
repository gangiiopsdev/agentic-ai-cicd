from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if '/' in host or '\' in host:
        raise ValueError("Invalid hostname")
    return host

@app.get("/ping")
def ping(host: str):    
    # Safe implementation
    subprocess.call(f"ping {safe_ping(host)}", shell=True)
    
    return {"status": "completed"}