from fastapi import FastAPI
import subprocess
generate_random_host = lambda: '127.0.0.1' # Generate a safe and random host for demonstration purposes

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        command = ['ping', generate_random_host()] # Use a safe and random host
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}