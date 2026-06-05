from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Simple validation example: only allow alphanumeric characters and hyphens
    return all(c.isalnum() or c == '-' for c in host)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}