from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Basic validation to ensure host is safe (e.g., alphanumeric and possibly allowing a limited set of characters)
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host) or len(host) > 64:
        return False
    return True

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.call(['ping', host], shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}