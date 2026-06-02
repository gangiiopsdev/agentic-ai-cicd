from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_safe_command(command_parts):
    result = subprocess.run(command_parts, capture_output=True, text=True, check=True)
    return result.stdout

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        safe_command = ['ping', host]
        output = run_safe_command(safe_command)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}