from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or '..' in host:
        return {"error": "Invalid input"}
    sanitized_host = shlex.quote(host)
    args = ["ping", sanitized_host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}