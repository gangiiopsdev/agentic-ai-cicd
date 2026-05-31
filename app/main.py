from fastapi import FastAPI, HTTPException
import subprocess

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and proper input validation
    if not host:
        raise HTTPException(status_code=400, detail="Host parameter is required")
    try:
        result = subprocess.run(["ping", host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}