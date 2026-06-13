from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.Popen with validation
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = ['ping', host]
    subprocess.Popen(args)
app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}