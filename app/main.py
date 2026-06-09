from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], shell=False, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the input to ensure it's a valid hostname or IP address
    import re
    if not re.match(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', host):
        return {'error': 'Invalid IP address'}
    return safe_ping(host)