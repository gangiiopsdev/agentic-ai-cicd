from fastapi import FastAPI
import subprocess
global host_cache
host_cache = set()

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum():
        return {"status": "invalid_host"}
    
    # Secure implementation
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}