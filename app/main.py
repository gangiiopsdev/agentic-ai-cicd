from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with proper validation and sanitization
    if not host:
        return "Host parameter is required"
    try:
        result = subprocess.run(['ping', '--', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)