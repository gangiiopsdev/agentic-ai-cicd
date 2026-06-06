from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host parameter to prevent command injection
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return {"status": "completed"}

# Example validation function (customize as needed)
def is_valid_host(host: str) -> bool:
    # Simple example that checks for alphanumeric characters and a single period
    return all(c.isalnum() or c == '.' for c in host) and host.count('.') == 1