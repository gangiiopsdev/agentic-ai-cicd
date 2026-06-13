from fastapi import FastAPI
import subprocess

global app
app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    result = subprocess.run(f'ping -c 1 {host}', capture_output=True, text=True)
    return {"status": "completed", "stdout": result.stdout, "stderr": result.stderr}