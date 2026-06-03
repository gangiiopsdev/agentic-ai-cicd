from fastapi import FastAPI, HTTPException
import subprocess

class SafeSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        return subprocess.run(command, *args, **kwargs)

app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize the host input
        if not host.strip():
            raise ValueError("Invalid host input")
        allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example list, update with actual allowed IPs
        if host not in allowed_hosts:
            raise ValueError("Invalid host input")
        # Use subprocess.run with separate arguments to prevent shell injection
        result = SafeSubprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except Exception as e:
        return {"status": "failed", "error": str(e)}