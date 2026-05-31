from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

async def safe_ping(host: str):
    if not host.isalnum():  # Basic validation
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping'] + shlex.split(host)
    try:
        result = await asyncio.subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return await safe_ping(host)