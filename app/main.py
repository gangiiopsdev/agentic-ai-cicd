from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

def validate_host(host: str) -> bool:
    # More robust host validation logic here, e.g., regex matching against allowed IP ranges or domain patterns
    return True  # Placeholder for actual validation

def sanitize_input(input_str: str) -> str:
    # Implement input sanitization logic here
    return input_str.strip()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not validate_host(sanitized_host):
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping', '--'] + [sanitized_host]  # Use -- to separate options from positional arguments
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}