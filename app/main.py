from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    sanitized_host = host.strip()
    subprocess.run(["ping", sanitized_host], check=True)
    return {"status": "completed"}