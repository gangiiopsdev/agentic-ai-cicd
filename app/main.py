from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input to prevent injection attacks
    if not host.isalnum():
        return "Invalid input"
    return {"status": safe_ping(host)}