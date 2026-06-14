from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return result.stdout.strip()

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if not host.isalnum():
        return {'error': 'Invalid input'}, 400
    try:
        response = safe_ping(host)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}, 500
    return {'status': 'completed', 'response': response}