from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}