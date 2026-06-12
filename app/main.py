from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    # Simple validation logic, can be enhanced based on requirements
    return all(c.isalnum() or c in ['.', '-'] for c in host)

def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host', 'status': 'failed'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}