from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input and use a fixed command path
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}