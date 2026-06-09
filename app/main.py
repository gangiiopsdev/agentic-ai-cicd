from fastapi import FastAPI
import subprocess
def escape_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in ['.', '-', '_'])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        escaped_host = escape_input(host)
        result = subprocess.run(['ping', escaped_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stderr': e.stderr}