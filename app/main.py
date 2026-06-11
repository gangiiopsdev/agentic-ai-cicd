from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    # Secure implementation
    safe_host = ''.join(c for c in host if c.isalnum() or c in ('.', '-', '_'))
    subprocess.call(["ping", safe_host])
    return {"status": "completed"}