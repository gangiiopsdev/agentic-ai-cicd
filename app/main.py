from fastapi import FastAPI
import subprocess
global app = FastAPI()
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e}'
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)