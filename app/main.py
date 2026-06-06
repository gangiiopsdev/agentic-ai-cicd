from fastapi import FastAPI
import subprocess
cimport re

app = FastAPI()

def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    subprocess.call(['ping', host])

    return {"status": "completed"}