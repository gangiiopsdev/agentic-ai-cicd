from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isdigit():
        raise ValueError('Invalid host parameter')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):    return {'status': 'completed'}