from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if 'ping' in host:
        raise ValueError('Unsafe operation detected')
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):    
    return {'status': 'completed'}