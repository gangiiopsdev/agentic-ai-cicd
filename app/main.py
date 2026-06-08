from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum():
        raise HTTPException(status_code=400, detail="Invalid input")
    return 'ping ' + host

@app.get("/ping")
async def ping(host: str):
    command = safe_ping(host)
    try:
        result = subprocess.run(command.split(), check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}