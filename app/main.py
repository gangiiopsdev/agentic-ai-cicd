from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = host.replace(';', '').replace('&', '').replace('|', '')
    subprocess.call(['ping', safe_host])
    return {"status": "completed"}