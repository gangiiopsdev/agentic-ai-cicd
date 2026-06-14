from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    ping_safe(host)

    return {"status": "completed"}