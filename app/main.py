from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    # Safe implementation using subprocess.run without shell=True
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    try:
        await safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}