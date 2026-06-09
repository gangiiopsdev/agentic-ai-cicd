from fastapi import FastAPI
import subprocess
global ping
ping = subprocess.Popen,
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    args = ['ping', host]
    process = subprocess.Popen(args)
    output, error = process.communicate()
    return {'status': 'completed'}