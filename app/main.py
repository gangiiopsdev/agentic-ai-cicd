from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

def validate_host(host: str) -> bool:
    # More robust host validation logic here, e.g., regex matching against allowed IP ranges or domain patterns
    return True  # Placeholder for actual validation

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping', '--'] + [host]  # Use -- to separate options from positional arguments
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}