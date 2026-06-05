from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host:
        return {"status": "error", "message": "Host parameter is required"}
    # Secure implementation using subprocess.run with shell=False and proper argument handling
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    if result.returncode != 0:
        return {
            "status": "error",
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    return {
        "status": "completed",
        "stdout": result.stdout,
        "stderr": result.stderr
    }