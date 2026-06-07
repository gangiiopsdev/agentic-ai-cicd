from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return result.stdout
    except subprocess.TimeoutExpired:
        return 'Ping timed out'

@app.get("/ping")
def ping(host: str):
    return {'status': safe_ping(host)}