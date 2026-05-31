from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize the host parameter
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return "Invalid input"
    try:
        result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return str(e)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)