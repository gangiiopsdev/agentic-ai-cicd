from fastapi import FastAPI
import subprocess
cimport = False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not cimport:
        cimport = True
        subprocess.call(['ping', host], shell=False, executable='/bin/ping')

    return {"status": "completed"}