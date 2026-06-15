from fastapi import FastAPI
import subprocess

def run_safe_ping(host):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return result.stdout

app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        output = run_safe_ping(host)
        return {'status': 'completed', 'output': output}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}