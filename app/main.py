from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping_safe(host: str):
    # Enhanced validation and sanitization
    if not re.match(r'^[0-9]+(?:\.[0-9]+){3}$', host) or '.' not in host:
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}