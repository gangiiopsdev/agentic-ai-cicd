from fastapi import FastAPI
import subprocess
def escape_host(host):
    return host.replace('`', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_host(host)
    try:
        subprocess.run(['ping', escaped_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

    return {'status': 'completed'}