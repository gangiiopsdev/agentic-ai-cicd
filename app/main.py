from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        result = subprocess.run(shlex.split(f'ping {shlex.quote(host)}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    import re
    host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
    return safe_ping(host)