from fastapi import FastAPI
import subprocess
global pinger

async def ping(host: str):
    global pinger
    try:
        pinger = subprocess.Popen(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = pinger.communicate()
        return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    return ping(host)

def is_safe_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    return host in allowed_hosts