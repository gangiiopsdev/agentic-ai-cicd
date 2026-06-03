from fastapi import FastAPI, HTTPException
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input to prevent injection attacks
    if not host.strip().isalnum() or len(host) > 255:
        raise HTTPException(status_code=400, detail='Invalid host')
    try:
        safe_host = shlex.quote(host)
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))