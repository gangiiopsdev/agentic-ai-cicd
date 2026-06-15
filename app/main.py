from fastapi import FastAPI
import subprocess
def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in ('.', ':', '-', '_'))

cmd = ['ping', host]
safe_cmd = [c.replace(';', '') for c in cmd]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.call(safe_cmd + [escaped_host])
    return {'status': 'completed'}