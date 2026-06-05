from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(char for char in input_str if char in allowed_chars)

app = FastAPI()

@app.get('/ping')
def ping(host: str):\n    sanitized_host = subprocess.quote(host)\n    try:\n        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)\n        return {'status': 'completed', 'output': result.stdout}\n    except subprocess.CalledProcessError as e:\n        return {'status': 'failed', 'error': str(e)}