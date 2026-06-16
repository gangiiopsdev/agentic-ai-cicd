from fastapi import FastAPI
import subprocess
from typing import Dict
from fastapi.responses import JSONResponse

app = FastAPI()

def sanitize_input(value: str) -> str:
    return ''.join(c for c in value if c.isalnum() or c in ('.', '-', '_'))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, timeout=10)
        return JSONResponse({'status': 'completed', 'output': output.decode()})
    except subprocess.CalledProcessError as e:
        return JSONResponse({'status': 'failed', 'error': e.output.decode()}, status_code=500)
    except TimeoutExpired:
        return JSONResponse({'status': 'timeout'}, status_code=504)