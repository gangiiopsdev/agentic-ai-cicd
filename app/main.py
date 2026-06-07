from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host in allowed_hosts:
        return subprocess.call(['ping', '--', host])
    else:
        return "invalid host"

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, int):
        return {'status': 'completed', 'exit_code': result}
    else:
        return {'status': result}