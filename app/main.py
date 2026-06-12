from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        raise ValueError('Invalid hostname')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.run(["ping", "-c", "1", host], check=True, shell=False)
    return {"status": "completed"}