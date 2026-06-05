from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host input"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    except TimeoutExpired:
        return {"status": "timeout", "message": "Command timed out"}
def validate_host(host: str) -> bool:
    # Simple validation to allow only alphanumeric and hyphen characters
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')
    return all(char in allowed_chars for char in host)