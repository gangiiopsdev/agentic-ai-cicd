from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise HTTPException(status_code=400, detail="Invalid input")
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}