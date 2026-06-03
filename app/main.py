from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more valid hosts as needed
    return host in allowed_hosts
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    # Secure implementation
    try:
        result = subprocess.run(["ping", host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}