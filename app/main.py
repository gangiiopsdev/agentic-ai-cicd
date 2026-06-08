from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host) or len(host) > 255:
        return {"status": "error", "message": "Invalid hostname"}
    subprocess.run(['ping', re.escape(host)], check=True)
    return {"status": "completed"}