from fastapi import FastAPI
import subprocess
def validate_host(host):
    if not host.strip() or len(host) > 255:
        return False
    return True
def sanitize_host(host):
    return ''.join(e for e in host if e.isalnum())
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return{"error": "Invalid host parameter"}, 400
    sanitized_host = sanitize_host(host)
    subprocess.call(["ping", sanitized_host])
    return {"status": "completed"}