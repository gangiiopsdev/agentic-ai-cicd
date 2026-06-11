from fastapi import FastAPI
import subprocess
import shlex

# Define global arguments securely
global_args = ['ping', 'example.com']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Sanitize input to avoid shell injection
        sanitized_host = shlex.quote(host)
        args = shlex.split(' '.join(global_args + [sanitized_host]))
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}