from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Enhanced sanitization to prevent command injection
    safe_host = ''.join(c for c in host if c.isalnum() or c in '-_.')
    if not safe_host:
        raise ValueError("Invalid input")
    subprocess.run(["ping", safe_host], check=True)
    return {"status": "completed"}