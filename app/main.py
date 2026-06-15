from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    # Implement your sanitization logic here
    return 'ping' if input_str == 'localhost' else None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = sanitize_input(host)
    if safe_host is None:
        return {"status": "failed", "error": "Invalid host"}, 400
    result = subprocess.run([safe_host, host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "output": result.stdout.decode()}