from fastapi import FastAPI
import asyncio
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Sanitize input by using a whitelist of allowed hosts
    if host not in ['example.com', 'localhost']:
        raise ValueError('Invalid host')
    args = ['ping', '-c', '1'] + shlex.split(host)
    result = asyncio.create_subprocess_exec(*args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.communicate()

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
    except Exception as e:
        return {'status': 'error', 'error': str(e)}