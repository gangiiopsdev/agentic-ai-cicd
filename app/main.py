from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host not in ['127.0.0.1', '::1']:  # Restrict hosts to localhost for safety
        raise ValueError('Invalid host')
    args = ['ping', '-c', '4', host]  # Use list of arguments instead of shell=True
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}