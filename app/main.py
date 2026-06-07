from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host or len(host) > 255:
        raise ValueError("Invalid host")

@app.get="/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], timeout=5, check=True, capture_output=True, text=True)
        return {"status": "completed", "result": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}