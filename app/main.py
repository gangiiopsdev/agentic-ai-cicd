from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation
    subprocess.call(['ping', host])
    return {'status': 'completed'}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)