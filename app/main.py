from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate the host input to ensure it does not contain malicious content
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        response = safe_ping(host)
        return {'status': 'completed', 'output': response}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}