from fastapi import FastAPI
import subprocess
def sanitize_host(host: str) -> str:
    # Simple sanitization example, replace with more robust validation
    return ''.join(e for e in host if e.isalnum() or e in ['.', '-'])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = ['ping', sanitized_host]
    subprocess.run(args, check=True, shell=False)  # Ensure shell=False to avoid injection
    return {"status": "completed"}