from fastapi import FastAPI
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-:_'
    if not all(c in allowed_chars for c in host) or re.search(r'[^a-zA-Z0-9.-_:]', host):
        raise ValueError("Invalid host input")
    try:
        result = subprocess.run(["/usr/bin/ping", "-c", str(1), host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}