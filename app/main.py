from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Simple validation, can be expanded based on requirements
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.run(['ping', host], check=True, shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 400