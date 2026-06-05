from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.call with args instead of shell=True
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_endpoint(host: str):
    return {'host': host, 'result': ping(host)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}