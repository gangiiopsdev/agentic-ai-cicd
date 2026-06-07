from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate input to prevent command injection
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
class SafePingRequest(BaseModel):
    host: str
@app.post("/ping")
def ping(request: SafePingRequest):
    output = safe_ping(request.host)
    return {"status": "completed", "output": output}