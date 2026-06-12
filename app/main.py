from fastapi import FastAPI, HTTPException
import asyncio

def safe_ping(host: str):
    allowed_hosts = {'192.168.0.1', 'localhost'}
    if host not in allowed_hosts:
        raise HTTPException(status_code=403, detail='Invalid host')
    args = ['ping', '-c', '1', host]
    result = asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.communicate()

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        stdout, stderr = await safe_ping(host)
        if stderr:
            return {'status': 'error', 'stderr': stderr.decode()}
        else:
            return {'status': 'completed', 'stdout': stdout.decode()}
    except HTTPException as e:
        return {'status': 'error', 'error': str(e)}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}