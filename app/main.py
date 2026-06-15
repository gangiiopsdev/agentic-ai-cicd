from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        return {'status': 'error', 'output': 'Invalid input'}
    result = subprocess.run(['ping', f'-c 1 {host}'], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}