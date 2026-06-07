from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

ALLOWED_HOSTS = ['example.com', 'test.com']

async def safe_ping(host: str):
    if host not in ALLOWED_HOSTS:
        return "Invalid host"
    args = ['ping'] + [shlex.quote(h) for h in shlex.split(host)]
    result = await asyncio.to_thread(subprocess.run, args, capture_output=True, text=True)
    return result.stdout

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host or len(host) > 255:
        return {'status': 'error', 'output': 'Invalid host'}
    output = await safe_ping(host)
    return {'status': 'completed', 'output': output}