from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate and sanitize the host input
    if not host.isdigit():
        return "Invalid host"
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'response': response}