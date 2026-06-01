from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Implement validation logic here (e.g., IP address, hostname format)
    allowed_hosts = ['localhost', '127.0.0.1']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        subprocess.call(['ping', host])
        return {"status": "completed"}
    else:
        return {"status": "error", "message": "Invalid host"}