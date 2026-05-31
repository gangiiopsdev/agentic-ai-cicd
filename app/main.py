from fastapi import FastAPI
import subprocess
def validate_host(host):
    # More comprehensive validation: allow only alphanumeric characters, hyphens, and periods
    return all(c.isalnum() or c in '-.' for c in host)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host name"}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}