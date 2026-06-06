from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.run
    subprocess.run(['ping', '-c', '1', host], check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):