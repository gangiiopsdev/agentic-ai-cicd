from fastapi import FastAPI
import subprocess
cimport = lambda cmd: subprocess.call(cmd, shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(cimport(f"ping {host}"))
    return {"status": "completed"}