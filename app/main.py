from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation
    args = ['ping', host]
    subprocess.call(subprocess.list2cmdline(args))

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}