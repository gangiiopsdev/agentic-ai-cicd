from fastapi import FastAPI
import subprocess
global_host = '127.0.0.1' # replace this with appropriate validation and sanitization logic

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host != global_host:
        raise ValueError('Invalid host')
    subprocess.call(f'ping {host}', shell=False)

    return {"status": "completed"}