from fastapi import FastAPI
import subprocess
globally_banned_hosts = ['example.com', 'test.com']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if host in globally_banned_hosts:
        raise ValueError('Banned host')
    # Use subprocess.run for better control and security
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}