from fastapi import FastAPI
import subprocess

app = FastAPI()

async def safe_ping(host):
    args = ['ping', '-c', '1', host]
    result = await asyncio.create_subprocess_exec(*args, capture_output=True, text=True)
    return result.stdout

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in ['example.com', 'test.com']:
        output = await safe_ping(host)
        return {'status': 'completed', 'output': output}
    else:
        return {'status': 'error', 'message': 'Invalid host'}