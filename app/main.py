from fastapi import FastAPI
import subprocess
cimport = 'ping {}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation without shell=True and format string usage
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}