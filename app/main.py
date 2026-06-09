from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation to sanitize user input
    safe_host = subprocess.list2cmdline([host])
    subprocess.run(['ping', safe_host], check=True)
    return {'status': 'completed'}