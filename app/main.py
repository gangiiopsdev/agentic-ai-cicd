from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def safe_ping(host: str):
    # Enhanced validation to prevent command injection
    if not re.match(r'^[a-zA-Z0-9]+$', host):
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        command = ['ping', subprocess.list2cmdline([host])]  # Use list2cmdline for shell-like behavior
        result = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        if result.returncode != 0:
            return {'status': 'error', 'message': f'Ping failed: {error.decode().strip()}'}
        return {'status': 'completed', 'output': output.decode().strip()}
    except Exception as e:
        return {'status': 'error', 'message': f'An error occurred: {e}'}

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)