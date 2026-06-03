from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_input(host):
    if not host.strip().isdigit():
        raise ValueError("Invalid host")
    return host

@app.get("/ping")
def ping(host: str):
    validated_host = validate_input(host)
    subprocess.call(['ping', validated_host])
    return {"status": "completed"}