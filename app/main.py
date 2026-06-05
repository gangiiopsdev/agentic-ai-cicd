from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.strip().isnumeric():
        return subprocess.call(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        raise ValueError('Invalid input')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        return {"status": safe_ping(host)}
    except ValueError as e:
        return {"error": str(e)}