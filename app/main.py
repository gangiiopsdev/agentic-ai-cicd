from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/ping")
def ping(host: str):    return {"result": safe_ping(host)}
def validate_host(host: str):
    # Add logic to validate the host parameter
    return True