from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command_parts):
    try:
        output = subprocess.run(command_parts, capture_output=True, text=True, check=True)
        return output.stdout.strip()
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command_parts = ['ping', host]
    sanitized_command_parts = [shlex.quote(part) for part in command_parts]
    output = run_command(sanitized_command_parts)
    return {'status': 'completed', 'output': output}