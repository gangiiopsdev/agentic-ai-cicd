from fastapi import FastAPI
import subprocess
import shlex
global_subprocess_env = {k: v for k, v in os.environ.items() if k in ['PATH', 'HOME']}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        subprocess.run(shlex.split(f'ping {host}'), check=True, env=global_subprocess_env, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
    return {'status': 'completed'}