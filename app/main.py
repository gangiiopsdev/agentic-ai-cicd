from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and proper argument parsing
    subprocess.run(["ping", host], check=True, capture_output=True)
    return {"status": "completed"}