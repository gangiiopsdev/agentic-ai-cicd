from fastapi import FastAPI
import subprocess
import shlex

def run_ping(host):
    try:
        # Using subprocess.run instead of subprocess.call for better security
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent OS command injection
    safe_host = ''.join(e for e in host if e.isalnum() or e in ('.', '-', '_'))
    return run_ping(safe_host)