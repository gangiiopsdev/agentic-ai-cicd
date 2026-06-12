from fastapi import FastAPI
import subprocess
from fastapi.encoders import jsonable_encoder
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ('.', '-', '_', '/'))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, timeout=5, check=True)
        return jsonable_encoder({'status': 'completed', 'output': result.stdout})
    except subprocess.CalledProcessError as e:
        return jsonable_encoder({'status': 'failed', 'error': e.stderr})