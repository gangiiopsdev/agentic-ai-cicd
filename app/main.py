from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid host name')
    ping_command = ['ping', shlex.quote(host)]  # Use shlex.quote() for safer subprocess execution
    subprocess.run(ping_command, check=True)

@app.get('/')</code><code>def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}