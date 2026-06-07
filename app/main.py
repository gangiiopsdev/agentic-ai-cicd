from fastapi import FastAPI
import subprocess
def safe_subprocess_call(command):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return e.stderr.decode()

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.strip():
        raise ValueError('Host cannot be empty')
    command = ['ping', '-c 1', host]
    return {'status': 'completed', 'output': safe_subprocess_call(command)}