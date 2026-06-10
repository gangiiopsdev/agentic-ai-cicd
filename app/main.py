from fastapi import FastAPI
import subprocess
import re

def sanitize_host(host):
    pattern = r'^[a-zA-Z0-9.-]{1,}$'
    return host if re.match(pattern, host) else ''

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        return {"status": "invalid input"}
    args = ['ping', sanitized_host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}