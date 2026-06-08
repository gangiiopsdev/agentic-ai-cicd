from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum() or len(host) > 255:
        raise HTTPException(status_code=400, detail="Invalid host parameter")
    # Use subprocess.run instead of subprocess.call for better control over arguments
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}