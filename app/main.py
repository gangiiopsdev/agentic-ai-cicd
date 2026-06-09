from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command_parts):
    try:
        result = subprocess.run(command_parts, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr.decode('utf-8')}'

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command_parts = ['ping', host]
    output = execute_command(command_parts)
    return {'status': 'completed', 'output': output}