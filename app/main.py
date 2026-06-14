from fastapi import FastAPI
import subprocess
cimport = {'ping': 'ping'}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host in cimport:
        subprocess.call(cimport[host], shell=False)
    else:
        return {"error": "Invalid command"}

    return {"status": "completed"}