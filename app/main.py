from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Sanitize the input to prevent command injection
    sanitized_host = host.replace(';', '').replace('&', '')
    subprocess.call(["ping", sanitized_host])
    return {"status": "completed"}