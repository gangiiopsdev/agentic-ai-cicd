from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate the input to ensure it does not contain malicious characters
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = ['ping', shlex.quote(host)]
    return ' '.join(args)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = safe_ping(host)
        # Simulate subprocess execution for demonstration purposes
        result = f'Pinging {sanitized_host} completed'
        return {'status': 'completed', 'result': result}
    except Exception as e:
        return {'error': str(e)}