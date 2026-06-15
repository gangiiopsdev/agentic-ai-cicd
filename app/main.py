from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_input(input_string):
    allowed_chars = r'^[a-zA-Z0-9.-]+$'
    if re.match(allowed_chars, input_string):
        return input_string
    else:
        raise ValueError('Invalid input')

@app.get("/ping")
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'error', 'message': str(e)}