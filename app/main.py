from fastapi import FastAPI
import subprocess

global app
app = FastAPI()

async def ping(host: str):
    # Safer implementation
    try:
        result = await subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get('/ping')
def ping_safe(host: str):
    return {'status': 'completed'}