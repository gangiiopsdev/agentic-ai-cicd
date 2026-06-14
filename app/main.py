from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safer implementation
    subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True)  # Using subprocess.run instead of subprocess.call
    return {"status": "completed"}