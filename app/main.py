from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Sanitize input to prevent command injection
    host = subprocess.quote(host)
    subprocess.call(['ping', host])
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}