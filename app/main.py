from fastapi import FastAPI
import subprocess
def execute_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate or sanitize the input
    if not host.isalnum():
        return {'error': 'Invalid input'}, 400
    command = ['ping', host]
    output = execute_command(command)
    return {'status': 'completed', 'output': output}