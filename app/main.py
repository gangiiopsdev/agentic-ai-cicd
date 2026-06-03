from fastapi import FastAPI
import subprocess

def safe_ping(host):
    # Validate and sanitize the host input
    if not isinstance(host, str) or not host.strip():
        raise ValueError('Invalid host input')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": "completed", "output": result}
    except ValueError as e:
        return {"status": "error", "message": str(e)}