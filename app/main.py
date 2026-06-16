from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except Exception as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it does not contain malicious content
    if not host.isalnum():
        return {"status": "error", "message": "Invalid input"}
    status = safe_ping(host)
    return {"status": "completed", "output": status}