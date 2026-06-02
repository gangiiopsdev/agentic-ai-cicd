from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.strip() and len(host.split('.')) == 4:
        subprocess.run(['ping', host], check=True, timeout=5)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}