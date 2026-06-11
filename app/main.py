from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Validate and sanitize the input
    if not host.strip().isdigit():
        raise ValueError('Invalid host input')
    args = ['ping', host]
    return subprocess.run(args, capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": "completed", "stdout": result.stdout}
    except ValueError as e:
        return {"status": "error", "message": str(e)}