from fastapi import FastAPI
import subprocess
def execute_command(command: str):
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, timeout=5, shell=True)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = ['ping', host]
    return execute_command(command)