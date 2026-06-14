from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        return {'error': 'Invalid input'}
    args = ['ping', host]
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate host input to avoid command injection
    if not host.isalnum() or not all(c in string.ascii_letters + string.digits for c in host):
        return {'error': 'Invalid input'}
    return safe_ping(host)