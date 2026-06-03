from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.run without shell=True
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed", "message": "Ping successful"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}