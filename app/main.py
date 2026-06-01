from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and explicitly splitting the command
    subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    return {'status': 'completed'}