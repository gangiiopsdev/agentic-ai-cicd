from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping_safe(host: str):
    # Secure alternative using subprocess.run with input validation
    if host.isalnum():
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "error", "message": "Invalid hostname"}