from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host in ['localhost', '127.0.0.1']:  # Allow only specific hosts for security reasons
        subprocess.call(['ping', host], shell=False)
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}