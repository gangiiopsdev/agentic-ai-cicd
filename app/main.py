from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input to prevent command injection
    if not host.isalnum():
        return {"status": "failed", "error": "Invalid input"}
    try:
        output = subprocess.check_output(['ping', '127.0.0.1'], stderr=subprocess.STDOUT, timeout=5)  # Replace with a fixed IP or use another method to prevent command injection
        return {"status": "completed", "output": output.decode()} 
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {"status": "failed", "error": str(e)}