from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input to ensure it's a safe hostname
    if not all(c.isalnum() or c in ('.', '-') for c in host):
        return {"status": "error", "message": "Invalid host name"}
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "output": result.stdout.decode('utf-8')}