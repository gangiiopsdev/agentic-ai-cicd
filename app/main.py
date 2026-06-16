from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(value):
    return ''.join(c for c in value if c.isalnum() or c in '-.\/')

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = shlex.quote(sanitize_input(host))
        result = subprocess.run(['ping', '-c 1', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except ValueError as e:
        return {'status': 'error', 'output': str(e)}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}