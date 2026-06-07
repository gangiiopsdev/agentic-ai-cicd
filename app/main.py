from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using check_output instead of call for better control over the subprocess execution.
    args = ['ping'] + shlex.split(host)
    try:
        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}  # Return the command output
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}  # Handle errors gracefully