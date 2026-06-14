from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run to prevent shell injection
    subprocess.run(['ping', host], shell=False)
    return {"status": "completed"}