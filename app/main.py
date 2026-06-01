from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in '-.:/_')

@app.get("/ping")
def ping(host: str):\n    sanitized_host = sanitize_input(host)\n    try:\n        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)\n        return {'status': 'completed', 'output': result.stdout}\n    except Exception as e:\n        return {'status': 'error', 'message': str(e)}