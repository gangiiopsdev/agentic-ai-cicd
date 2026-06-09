from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(filter(lambda x: x.isalnum() or x in '._-', input_str))

async def run_ping(host):\n    sanitized_host = sanitize_input(host)\n    try:\n        result = subprocess.run(['ping', '-c', '1', sanitized_host], shell=False, capture_output=True, text=True)\n        return {'status': 'completed', 'output': result.stdout}\n    except Exception as e:\n        return {'status': 'error', 'message': str(e)}

@app.get('/ping')\ndef ping(host: str):\n    if not all(c.isalnum() or c in '._-' for c in host):\n        return {'status': 'error', 'message': 'Invalid input'}\n    return run_ping(host)