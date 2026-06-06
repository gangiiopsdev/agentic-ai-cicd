from fastapi import FastAPI
import asyncio
from shlex import quote
from fastapi.responses import JSONResponse
from subprocess import Popen, PIPE

async def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = ['ping', '-c', '1'] + [quote(host)]  # Use ping -c to limit the number of pings and ensure arguments are quoted separately
    try:
        result = await asyncio.to_thread(Popen, args, stdout=PIPE, stderr=PIPE)
        output, error = await asyncio.to_thread(result.communicate)
        return {'output': output.decode('utf-8')}
    except Exception as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = await safe_ping(host)
    if isinstance(result, dict) and 'error' in result:
        return JSONResponse(status_code=400, content={'status': 'failed', 'error': result['error']})
    else:
        return {'status': 'completed', 'output': result['output']}