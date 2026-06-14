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
        result = cimport(f'ping {host}', capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}

# Preventive controls:
# 1. Validate and sanitize input before passing it to subprocess.
# 2. Use a safer alternative like `subprocess.call` if possible.
# 3. Consider using a library designed for safe command execution, such as `shlex.quote`.