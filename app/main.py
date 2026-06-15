from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, shell=False)
    return result.stdout
global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if 'localhost' not in host and '127.0.0.1' not in host:
        raise ValueError('Only localhost is allowed')
    return safe_ping(host)
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}