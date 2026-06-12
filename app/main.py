from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_endpoint(host: str):
    return {'host': host, 'result': ping(host)}

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}