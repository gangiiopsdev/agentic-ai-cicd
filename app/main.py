from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    safe_host = host.replace(';', '').replace('&', '')
    subprocess.call(['ping', safe_host])
    return {"status": "completed"}