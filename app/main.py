from fastapi import FastAPI
cimport subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host to prevent command injection
    if not host.isalnum() and '-' not in host:
        raise ValueError('Invalid host name')
    subprocess.run(['ping', '--param', host], check=True, capture_output=True)
    return {'status': 'completed'}