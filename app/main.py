from fastapi import FastAPI
import asyncio
import shlex

def validate_host(host: str) -> bool:
    # Simple validation example, replace with appropriate logic
    return host.isnumeric()

async def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host provided')
    args = ['ping', '-c', '1', shlex.quote(host)]
    result = await asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = await result.communicate()
    return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_route(host: str):
    return ping(host)