from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.isalnum():
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid hostname')

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    safe_ping(host)

    return {"status": "completed"}