from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and safe arguments
    if not host.isalnum():
        return {"status": "failed", "output": "Invalid input"}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    if result.returncode != 0:
        return {"status": "failed", "output": result.stderr}
    return {"status": "completed", "output": result.stdout}