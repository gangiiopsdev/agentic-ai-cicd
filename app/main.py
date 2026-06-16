from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Implement validation logic for host
    return True

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"error": "Invalid host"}
    
    # Fixed implementation
    subprocess.call(f"ping {host}", shell=False)
    
    return {"status": "completed"}