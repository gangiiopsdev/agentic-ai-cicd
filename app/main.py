from fastapi import FastAPI
import subprocess
from typing import Dict

app = FastAPI()

async def sanitize_input(input_str: str) -> str:
    # More robust sanitization using allowed characters
    return ''.join(e for e in input_str if e.isalnum() or e in ['-', '.', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

@app.get("/ping")
def ping(host: str) -> Dict[str, str]:
    sanitized_host = await sanitize_input(host)
    # Using subprocess.run instead of subprocess.call and avoiding shell=True
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'completed', 'output': result.stdout}