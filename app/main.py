from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def safe_ping(host):
    # Sanitize input using regex to allow only alphanumeric characters and a limited set of allowed hosts
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or host not in ['example.com', 'test.com']:
        return None

    args = ['ping', '-c', '1', host]
    result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
    return result.stdout

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    output = await safe_ping(host)
    if output is not None:
        return {'status': 'completed', 'output': output}
    else:
        return {'status': 'error', 'message': 'Invalid host'}