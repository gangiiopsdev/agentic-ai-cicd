from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    # Safe implementation using list to avoid shell=True and validate input
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    ping_safe(host)
    return {"status": "completed"}