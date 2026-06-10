from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Implement validation logic for host input
    return host.replace('.', '').isalnum()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host input')
    # Safe implementation using subprocess.run with shell=False
    subprocess.call(['ping', host])
    return {"status": "completed"}