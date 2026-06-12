from fastapi import FastAPI
import asyncio
import re

app = FastAPI()

async def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    args = ['ping', '-c', '1', host]
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return await result.communicate()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        stdout, stderr = safe_ping(host)
        if stderr:
            return {'status': 'error', 'stderr': stderr.decode()}
        else:
            return {'status': 'completed', 'stdout': stdout.decode()}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}