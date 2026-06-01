from fastapi import FastAPI
import subprocess

app = FastAPI()

async def is_valid_host(host):
    # Basic validation: allow only alphanumeric characters and hyphens
    return host.replace('-', '').isalnum()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid hostname")
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}