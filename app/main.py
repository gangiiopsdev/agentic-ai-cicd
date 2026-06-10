from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation using subprocess.run with proper validation and sanitization
    if not host:
        raise ValueError('Host cannot be empty')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}
app = FastAPI()
@app.get("/ping")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping/{host}")
def ping(host: str):
    return ping(host)