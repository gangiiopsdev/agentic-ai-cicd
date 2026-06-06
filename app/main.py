from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Sanitize input to prevent command injection
    if not host.replace('.', '').isnumeric():
        raise ValueError('Invalid host format')
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    return {'status': result}