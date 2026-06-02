from fastapi import FastAPI
import subprocess

async def ping(host: str):
    try:
        # Sanitize the input to avoid shell injection
        if not all(char.isalnum() or char in ['-', '.'] for char in host):  # Validate input
            return {'status': 'failed', 'error': 'Invalid input'}
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping_handler(host: str):
    return await ping(host)