from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/)")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Secure implementation using subprocess.run with check=True to raise an exception on error
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

# Import the necessary module to sanitize inputs
from fastapi import FastAPI, HTTPException
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Define a regular expression pattern for allowed characters
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        raise HTTPException(status_code=400, detail="Invalid input")

    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}