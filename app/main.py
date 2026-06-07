from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        if '/' in host or '\' in host or ':' in host or '`' in host or ';' in host or '$' in host or '&' in host:
            raise ValueError('Invalid hostname')
        result = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if '/' in host or '\' in host or ':' in host or '`' in host or ';' in host or '$' in host or '&' in host:
        raise ValueError('Invalid hostname')
    result = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}