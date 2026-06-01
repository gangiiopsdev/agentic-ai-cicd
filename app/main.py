from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Validate and sanitize host to prevent injection attacks
    if not all(c.isalnum() or c in ('.', '-') for c in host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    result = subprocess.call(args)
    return result

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
    except ValueError as e:
        return {"status": "error", "message": str(e)}
    else:
        return {"status": "completed", "result": result}