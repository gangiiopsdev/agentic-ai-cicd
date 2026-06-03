from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Simple sanitization example: allow only alphanumeric characters and dots
    return ''.join(c for c in host if c.isalnum() or c == '.').rstrip('.').strip('.')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True, shell=False)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}