from fastapi import FastAPI
import subprocess

app = FastAPI()

async def validate_host(host: str) -> bool:
    # Simple host validation logic
    return all(c.isalnum() or c in ['.', '-'] for c in host)

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host input')

    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}