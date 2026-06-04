from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host:
        return {"status": "error", "message": "Host parameter is required"}
    # Secure implementation using subprocess.run with shell=False and proper argument handling
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {
        "status": "completed",
        "stdout": result.stdout,
        "stderr": result.stderr
    }