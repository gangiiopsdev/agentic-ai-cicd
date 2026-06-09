from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in host if char in allowed_chars)

@app.get("/ping")
def ping(host: str):
    # Sanitize input
    sanitized_host = sanitize_input(host)
    if not sanitized_host.strip() or len(sanitized_host) > 255:
        return {"status": "error", "message": "Invalid hostname"}

    # Secure implementation with complete path
    subprocess.call(["/bin/ping", sanitized_host])
    return {"status": "completed"}