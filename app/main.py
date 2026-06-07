from fastapi import FastAPI
import subprocess
cimport = ['ping']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host.strip().endswith(('.', '0', '127.0.0.1')):
        safe_host = subprocess.list2cmdline([host])
        subprocess.run(cimport + [safe_host], check=True)
    else:
        return {"status": "Invalid host"}

    return {"status": "completed"}