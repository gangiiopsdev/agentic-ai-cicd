from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input to prevent command injection
    if 'ping' not in host or '..' in host:
        raise ValueError('Invalid host')
    try:
        result = subprocess.run(['ping', '--', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {"status": "completed", "output": result.stdout + result.stderr}
    except Exception as e:
        return {"status": "failed", "error": str(e)}