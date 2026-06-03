from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Safe implementation using Popen
        args = ['ping', host]
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with error code {e.returncode}'}
    return {'status': 'completed'}