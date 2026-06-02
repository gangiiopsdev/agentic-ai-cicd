from fastapi import FastAPI
import subprocess
import re
def safe_ping(host: str):
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True, shell=False)
    return result.stdout

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent shell injection
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._:@:')
    if not re.match(r'^[a-zA-Z0-9-._:@:]+$', host):
        raise ValueError("Invalid characters in host")
    output = safe_ping(host)
    return {"status": "completed", "output": output}