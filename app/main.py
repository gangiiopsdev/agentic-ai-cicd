from fastapi import FastAPI
import subprocess
cimport = ('ping', 'google.com')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in cimport:
        raise ValueError("Invalid host")
    subprocess.call(host, shell=False)
    return {"status": "completed"}