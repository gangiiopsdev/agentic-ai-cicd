from fastapi import FastAPI
import subprocess

def execute_ping(host: str):
    try:
        # Validate and sanitize the host input
        if '.' in host and len(host.split('.')) == 4 and all(x.isdigit() for x in host.split('.')):
            args = ['ping', host]
            result = subprocess.run(args, check=True, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        else:
            return {'status': 'failed', 'error': 'Invalid host format'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return execute_ping(host)