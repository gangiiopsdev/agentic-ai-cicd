from fastapi import FastAPI
import subprocess
import shlex
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
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with error: {e.stderr}' if hasattr(e, 'stderr') else str(e)}