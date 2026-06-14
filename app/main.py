from fastapi import FastAPI
import subprocess
cimport = ['ping']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host not in cimport:
        return {"status": "invalid host", "error": "Invalid host provided"}
    subprocess.call(["ping", host])
    return {"status": "completed"}