from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation with full command and shell=False
    subprocess.run(['ping', host], check=True, capture_output=True)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    response = ping(host)
    return {"status": "completed"}