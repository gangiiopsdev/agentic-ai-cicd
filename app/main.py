from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    try:
        args = ['ping', shlex.quote(host)]  # Use shlex.quote to sanitize the input
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}