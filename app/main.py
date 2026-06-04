from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize host input
    if not host.isalnum():
        raise ValueError("Invalid host")
    args = ['ping', '" + \\"'.join(host.split()) + '"']
    result = subprocess.call(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        status = safe_ping(host)
    except ValueError as e:
        return {"error": str(e)}
    return {"status": "completed", "output": status}