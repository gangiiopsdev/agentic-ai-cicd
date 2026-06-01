from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define allowed hosts
    if host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping(host: str):

    # Sanitize input
    if not sanitize_host(host):
        raise ValueError("Invalid host")

    # Safe implementation without shell=True
    subprocess.call(['ping', host])

    return {"status": "completed"}