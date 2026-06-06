from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if host in ['localhost', '127.0.0.1']:
        # Safe hosts, allow ping
        subprocess.run(['ping', host], shell=False)
    else:
        raise ValueError('Unsafe host for ping')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}