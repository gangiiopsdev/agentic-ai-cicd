from fastapi import FastAPI
import subprocess
global host_whitelist = ['127.0.0.1', '::1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in host_whitelist:
        subprocess.call(f'ping {host}', shell=True)
    else:
        raise Exception('Unauthorized host')
    return {"status": "completed"}