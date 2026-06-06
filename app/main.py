from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host: str):
    # Validate the host to ensure it does not contain malicious characters or patterns.
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    if not all(c in allowed_chars for c in host):
        return "Invalid hostname"

    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "output": result}