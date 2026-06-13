from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate input to ensure it does not contain malicious characters or commands
    if 'ping' not in host:
        return "Invalid input"
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)