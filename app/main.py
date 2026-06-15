from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize the host input to avoid command injection
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized_host = ''.join(c for c in host if c in allowed_chars)
    try:
        output = subprocess.run(['/usr/bin/ping', sanitized_host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

gl_app = FastAPI()

@gl_app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}