from fastapi import FastAPI
import subprocess
cimport = subprocess.run

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate and sanitize input before passing it to subprocess
        host = subprocess.quote(host)
        result = cimport(f'ping {host}', capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}