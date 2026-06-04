from fastapi import FastAPI
import subprocess
def run_ping(host: str):
    # Validate and sanitize host input
    if not host.isalnum():
        raise ValueError('Invalid host input')
    result = subprocess.run(['ping', host], check=True, capture_output=True)
    return result.stdout.decode()
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        output = run_ping(host)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}