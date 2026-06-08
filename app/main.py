from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    # Use subprocess.run instead of subprocess.call for better control and security
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}