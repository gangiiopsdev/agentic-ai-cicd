from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Ensure host is a valid IP or hostname
    if not re.match(r'^[0-9]{1,3}\.[0-9]{1,3}\.\[0-9]{1,3}\.\[0-9]{1,3}$', host) and not validate_hostname(host):
        raise ValueError('Invalid host')
    subprocess.call(['ping', host])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        return safe_ping(host)
    except ValueError as e:
        return {'error': str(e)}, 400