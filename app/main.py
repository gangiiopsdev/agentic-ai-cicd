from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize input to prevent code injection
    if not host.strip().isalnum():
        return {"status": "error", "message": "Invalid input"}
    # Use a safer method to execute commands
    result = subprocess.run(["ping", host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input further if necessary
    try:
        int(host)
        return {"status": "error", "message": "Invalid input"}
    except ValueError:
        pass
    return safe_ping(host)