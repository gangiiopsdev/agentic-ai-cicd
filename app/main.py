from fastapi import FastAPI
import subprocess
cimport = subprocess.call
cdef ping(host: str):
    try:
        cimport(f"ping {host}", shell=False)
    except Exception as e:
        return {"error": str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)