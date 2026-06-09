from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    # Use subprocess.run instead and avoid shell=True
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    try:
        ping_safe(host)
        return {"status": "completed", "message": "Ping successful"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}