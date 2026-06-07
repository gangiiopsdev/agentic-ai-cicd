from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation with robust validation and sanitization
    if re.match(r'^[a-zA-Z0-9.-]{1,255}$', host) is None:
        raise ValueError('Invalid input for host')
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.stderr}