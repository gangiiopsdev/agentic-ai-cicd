from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host.isalnum():
        subprocess.call(['ping', host])
    else:
        return 'Invalid input'

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}