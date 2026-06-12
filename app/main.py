from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_command(command, *args):
    try:
        result = subprocess.run([command] + list(args), capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    output = execute_command('ping', host)
    return {'status': 'completed' if output else 'failed', 'output': output}