from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(filter(lambda x: x.isalnum() or x in '._-!', input_str))

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_input(host)
        result = subprocess.run(['ping', shlex.quote(sanitized_host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}