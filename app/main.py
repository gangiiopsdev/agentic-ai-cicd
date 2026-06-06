from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with check=True and capture_output=True
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True)
    return {"status": "completed", "output": result.stdout.decode()}