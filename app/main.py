from fastapi import FastAPI
import subprocess
guardrails = ['ping', '--count=1']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid host'}
    command = guardrails + [host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}