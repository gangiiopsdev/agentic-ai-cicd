from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()
@app.get("/ping")
def ping(host: str):    
    # Validate and sanitize the input
    if not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError("Invalid host name")
    safe_ping(host)
    return {"status": "completed"}