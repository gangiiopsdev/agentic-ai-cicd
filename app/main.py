from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation
    if validate_host(host):
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    else:
        return {"status": "host_not_allowed"}