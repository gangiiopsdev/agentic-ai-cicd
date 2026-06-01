from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    # Sanitize the host input to prevent injection
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        raise ValueError("Invalid host name")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        return safe_ping(host)
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}