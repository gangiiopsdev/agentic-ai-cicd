from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    return ''.join(char for char in input_str if char.isalnum() or char in ['.', '-', '_'])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    # Use shlex.quote to safely escape command arguments
    import shlex
    try:
        output = subprocess.check_output(['ping', shlex.quote(sanitized_host)], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}