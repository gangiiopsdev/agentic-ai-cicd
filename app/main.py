from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to ensure it does not contain malicious characters.
    if 'ping' in host or '&' in host or '|' in host:
        raise HTTPException(status_code=400, detail="Invalid input detected")

    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}