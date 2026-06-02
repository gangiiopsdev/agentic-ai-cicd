from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str):
    # Simple validation to allow only alphanumeric characters and hyphens
    return all(c.isalnum() or c == '-' for c in host)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host input"}
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}