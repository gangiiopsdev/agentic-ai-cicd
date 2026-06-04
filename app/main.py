from fastapi import FastAPI
import subprocess
from shlex import quote

async def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = ['ping', '-c', '1', quote(host)]  # Use ping -c to limit the number of pings
    try:
        result = await asyncio.subprocess.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = await result.communicate()
        return {'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = await safe_ping(host)
    if isinstance(result, dict) and 'error' in result:
        return {'status': 'failed', 'error': result['error']}
    else:
        return {'status': 'completed', 'output': result['output']}