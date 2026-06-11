from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Sanitize the host parameter to prevent command injection
    if not isinstance(host, str) or '&&' in host or ';' in host or '`' in host or '|' in host:
        raise ValueError('Invalid host input')
    # Use subprocess.run instead of subprocess.call for better control and security
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        output = safe_ping(host)
        return {"status": "completed", "output": output}
    except ValueError as e:
        return {"status": "error", "message": str(e)}