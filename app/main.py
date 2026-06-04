from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize host input to avoid command injection
    if not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError('Invalid characters in hostname')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}