from fastapi import FastAPI
import subprocess
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)
@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}