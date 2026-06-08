from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation using subprocess.run
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        ping(host)
        return {"status": "completed", "message": "Ping successful"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}