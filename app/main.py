from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation using check_output and splitting arguments
    result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
    return {'status': 'completed', 'result': result.decode()}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    return ping(host)