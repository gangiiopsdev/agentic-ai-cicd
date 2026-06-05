from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent injection attacks
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}