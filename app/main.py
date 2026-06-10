from fastapi import FastAPI
import subprocess
global host_whitelist
host_whitelist = ['127.0.0.1', '::1']

app = FastAPI()

def is_host_allowed(host):
    return host in host_whitelist

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_host_allowed(host):
        raise HTTPException(status_code=403, detail="Host not allowed")
    # Secure implementation
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}