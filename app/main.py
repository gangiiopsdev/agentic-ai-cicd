from fastapi import FastAPI
import subprocess
from fastapi import HTTPException
import re

async def safe_ping(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=422, detail='Invalid hostname')
    try:
        output = await asyncio.create_subprocess_exec('ping', host, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await output.communicate()
        if output.returncode != 0:
            raise Exception(stderr.decode())
        return {'status': 'completed', 'output': stdout.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return await safe_ping(host)