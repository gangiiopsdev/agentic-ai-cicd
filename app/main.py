from fastapi import FastAPI
import re

app = FastAPI()

async def ping(host: str):
    generate_ping_command = ['ping', host]
    # Validate the host input to ensure it does not contain malicious content
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    await asyncio.create_subprocess_exec(*generate_ping_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}

async def is_valid_host(host: str) -> bool:
    # Enhanced validation using regular expression
    allowed_chars = r'^[a-zA-Z0-9.-_]+$'
    return re.match(allowed_chars, host) is not None

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return await ping(host)