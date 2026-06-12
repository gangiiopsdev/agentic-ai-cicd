from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Sanitize input to prevent command injection
    args = ['ping', host.replace(' ', '')]
    return subprocess.run(args, capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if not host.isalnum():
        return {"error": "Invalid host parameter"}
    result = safe_ping(host)
    return {"status": "completed", "output": result.stdout}