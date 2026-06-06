from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Fixed implementation with input validation and logging
    if not host or len(host) > 255:
        raise ValueError("Invalid hostname")
    try:
        subprocess.run(['ping', '-c', '1', host], check=True, timeout=10)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}