from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

def ping_safe(host: str):
    # Validate and sanitize the input
    if not host.isalnum():
        raise HTTPException(status_code=400, detail="Invalid input")
    try:
        result = subprocess.run(['ping', '-c 1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f'Ping failed: {e.stderr}')

@app.get("/ping")
def ping(host: str):
    return ping_safe(host)