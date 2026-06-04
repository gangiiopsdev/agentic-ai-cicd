from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize input to prevent command injection
    args = ['ping', host.replace(';', ' ')]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout,

app = FastAPI()

@app.get("/ping")
def ping(host: str):    return safe_ping(host)