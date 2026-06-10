from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host in ['127.0.0.1', 'localhost']:  # Whitelist specific hosts
        subprocess.call(['ping', host])
    else:
        raise ValueError('Host not allowed')

@app.get("/ping")
def ping(host: str):  
    safe_ping(host)
    return {"status": "completed"}