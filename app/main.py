from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Fixed implementation
    subprocess.run(['ping', host], check=True)