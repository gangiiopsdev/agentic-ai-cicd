from fastapi import FastAPI
import subprocess
def run_safe_command(command, *args):
    return subprocess.check_output([command] + list(args), stderr=subprocess.STDOUT)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        output = run_safe_command('ping', host)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}