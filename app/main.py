from fastapi import FastAPI
import subprocess
cimport = 'ping {host}'

app = FastAPI()

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.run([cimport], shell=False, check=True)
    return {"status": "completed"}