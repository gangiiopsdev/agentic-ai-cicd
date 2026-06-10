from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    # Validate input to prevent command injection
    if not host.strip().replace('.', '').isdigit():
        raise ValueError("Invalid host format")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}