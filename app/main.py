from fastapi import FastAPI
import subprocess
import shlex
def shell_escape(s):
    return ''.join([c if c.isalnum() or c in '._-:/\' else \\u%04x' % ord(c) for c in s])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        command = ['ping'] + shlex.split(shell_escape(host))
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}