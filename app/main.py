from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    try:
        # Validate and sanitize the input
        if not host.isalnum():
            return {'status': 'failed', 'error': 'Invalid host'}
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return execute_ping(host)