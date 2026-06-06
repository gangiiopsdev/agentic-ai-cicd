from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', '-c', '1', host], check=True, timeout=5)
    return {"status": "completed"}