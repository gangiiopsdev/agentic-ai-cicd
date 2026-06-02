from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def safe_ping(host):
    if re.match(r'^[a-zA-Z0-9.-]+$', host):
        await asyncio.create_subprocess_exec('ping', host, check=True)
    else:
        raise ValueError('Invalid characters in hostname')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        await safe_ping(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e), 'status': 'failed'}