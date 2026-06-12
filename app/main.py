from fastapi import FastAPI
import subprocess

app = FastAPI()

def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in ('.', ':', '-', '_'))

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_host(host)
    args = ['ping', escaped_host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}