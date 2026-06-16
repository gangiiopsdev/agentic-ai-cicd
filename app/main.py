from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():  # Basic validation to prevent injection
        return {
            "status": "error",
            "message": "Invalid input"
        }
    result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    return {
        "status": "completed",
        "output": result.stdout,
        "error": result.stderr
    }