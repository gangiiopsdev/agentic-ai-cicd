from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    return host.isalnum()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host input"}
    subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    return {"status": "completed"}