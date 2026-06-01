from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid host name'}, 400
    # Use shlex.split to safely split the command into a list of arguments
    try:
        result = subprocess.run(shlex.split('ping ' + host), check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}, 500