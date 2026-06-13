from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get("/ping")
def ping_safe(host: str):
    # Validate and sanitize the input
    if not host.isalnum():
        raise HTTPException(status_code=400, detail="Invalid input")
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f'Ping failed: {e.stderr}')