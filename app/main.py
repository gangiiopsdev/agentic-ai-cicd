from fastapi import FastAPI
import subprocess
cimport shlex
cimport os

cdef ping(host: str):
    cdef list args = shlex.split(f"ping {host}")
    subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping(host)
    return {"status": "completed"}