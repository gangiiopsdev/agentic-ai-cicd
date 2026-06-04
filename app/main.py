from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['localhost']
    if host in allowed_hosts:
        return True
    else:
        return False

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        args = ['ping', host]
        subprocess.call(args, shell=False)  # Ensure shell=False to prevent shell injection
        return {"status": "completed"}
    else:
        return {"status": "error", "message": "Invalid host"}