from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Use subprocess.run to avoid shell injection
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}