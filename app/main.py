from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with shell=False and check=True
    try:
        subprocess.run(['ping', host], check=True, shell=False)
    except Exception as e:
        raise ValueError(f"Ping failed: {str(e)}")

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e), "status": "failed"}