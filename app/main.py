from fastapi import FastAPI
import subprocess
def run_safe_command(command, *args):
    try:
        output = subprocess.run(command.split(), check=True, capture_output=True, text=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f'Error: {e.stderr}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    command = ['ping', host]
    result = run_safe_command(*command)
    return {'status': 'completed', 'result': result}