from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not all(c.isalnum() or c in '.-_' for c in host):
        return "Invalid hostname"
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)