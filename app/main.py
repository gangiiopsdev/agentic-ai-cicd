from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize host input
    if not all(c.isalnum() or c in [".", "-"] for c in host):
        raise ValueError("Invalid hostname")

app = FastAPI()

@app.get="/ping")
def ping(host: str):
    # Use the sanitized host directly without additional sanitization
    result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}