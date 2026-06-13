from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

def safe_ping(host: str) -> str:
    # Validate input to ensure it is safe to ping
    if not host.isalnum():
        raise ValueError("Invalid host name")
    try:
        result = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'result': result.decode()}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)