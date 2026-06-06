from fastapi import FastAPI
import shlex
def safe_ping(host: str):
    if not host.isdigit():
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping'] + [arg for arg in shlex.split(host) if arg.isdigit()]
    return {'status': 'completed', 'output': ' '.join(args)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)