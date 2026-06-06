from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Sanitize host to prevent command injection
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
    else:
        raise ValueError('Host not allowed')

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        output = safe_ping(host)
        return {'status': 'completed', 'output': output}
    except ValueError as e:
        return {'error': str(e)}