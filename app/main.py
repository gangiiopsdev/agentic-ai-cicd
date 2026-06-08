from fastapi import FastAPI
import subprocess
ALLOWED_HOSTS = ['example.com', 'another-example.com']

async def safe_ping(host: str):
    # Check if host contains malicious characters
    if any(char in host for char in [';', '&', '|', '(', ')']):
        return {'status': 'error', 'message': 'Invalid input'}
    # Use a whitelist of allowed hosts or use a safe method to validate the input
    if host not in ALLOWED_HOSTS:
        return {'status': 'error', 'message': 'Invalid input'}

    try:
        output = await asyncio.subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'success', 'message': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
global app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)