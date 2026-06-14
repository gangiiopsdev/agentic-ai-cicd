from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host.isdigit():
        raise ValueError('Invalid host input')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        subprocess.call(['ping', host])
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}, 400