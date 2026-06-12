from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with validation and sanitization
    if not host.isalnum():
        return {"status": "error", "output": "Invalid input"}
    result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}