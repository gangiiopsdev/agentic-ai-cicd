from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host.strip():
        raise ValueError("Host cannot be empty")
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    if not all(c in allowed_chars for c in host):
        raise ValueError("Invalid characters in host name")

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        validate_host(host)
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except ValueError as e:
        return {"status": "failed", "error": str(e)}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}