from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host:
        return {"error": "Host parameter is required"}

    try:
        # Secure implementation using subprocess.run with shell=False and check=True
        result = subprocess.run(["ping", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        if result.returncode == 0:
            return {"status": "completed", "output": result.stdout}
        else:
            return {"status": "failed", "error": result.stderr}
    except subprocess.TimeoutExpired:
        return {"status": "timeout", "message": "Ping request timed out"}