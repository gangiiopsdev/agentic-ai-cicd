from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in '-.' for c in host):
        return {'error': 'Invalid hostname'}
    return {'status': safe_ping(host)}