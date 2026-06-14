from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Using subprocess.run with a list avoids shell=True and mitigates the risk
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent malicious commands
    if not all(c.isalnum() or c in ('.', '-') for c in host):  # Basic validation
        return {'error': 'Invalid host'}, 400
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}