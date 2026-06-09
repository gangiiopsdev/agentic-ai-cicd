from fastapi import FastAPI
import subprocess
gimport shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        args = shlex.split(f'ping {shlex.quote(host)}')  # Use shlex.quote to sanitize the input
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with error: {e}'}

    return {'status': 'completed'}