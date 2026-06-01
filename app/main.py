from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True, shell=False)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    # Validate the input to prevent shell injection\n    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._:@:')\n    if not all(c in allowed_chars for c in host):\n        raise ValueError("Invalid characters in host")\n    output = safe_ping(host)\n    return {"status": "completed", "output": output}