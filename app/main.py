from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation using subprocess.run with whitelisting and validation
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/ping')
def ping_secure(host: str):
    return await ping(host)

# Helper function to validate host input
async def is_valid_host(host: str) -> bool:
    # Simple validation, more complex logic can be implemented based on requirements
    return all(c.isalnum() or c in ['-', '.', '_'] for c in host)