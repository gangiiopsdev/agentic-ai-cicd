from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if 'ping' in host:
        return {'error': 'Invalid input'}, 400
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e), 500

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)