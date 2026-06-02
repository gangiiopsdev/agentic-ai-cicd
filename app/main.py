from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Use shlex to properly escape the host input
        output = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.TimeoutExpired:
        return {'status': 'timeout'}