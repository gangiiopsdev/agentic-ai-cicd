from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input to prevent injection attacks
    if not host.isalnum():
        return {"status": "error", "result": "Invalid host name"}
    result = safe_ping(host)
    return {"status": "completed", "result": result}