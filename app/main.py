from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Validate input
    if not host.strip() or len(host) > 256:
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        output = await asyncio.subprocess.run(['ping', '-c', '4', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    # Validate input
    if not host.strip() or len(host) > 256:
        return {'status': 'failed', 'error': 'Invalid host name'}
    return await ping(host)