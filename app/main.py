from fastapi import FastAPI
import subprocess


global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or '..' in host:
        return {"error": "Invalid hostname"}, 400
    result = subprocess.run(f'ping -c 1 {host}', capture_output=True, text=True)
    return {"status": "completed", "stdout": result.stdout, "stderr": result.stderr}