from fastapi import FastAPI
import subprocess
cimport socket

app = FastAPI()

def is_valid_host(host: str) -> bool:
    try:
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if is_valid_host(host):
        subprocess.call(['ping', host])
    else:
        return {"status": "invalid host"}
    return {"status": "completed"}