from fastapi import FastAPI
import subprocess
generate_random_payload = 'ping' # Replace with a safe payload or method

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in ['127.0.0.1', '::1']:
        return {'status': 'error', 'message': 'Invalid host'}

    # Safe payload execution
    cmd = [generate_random_payload, '127.0.0.1']  # Use hardcoded safe input
    subprocess.run(cmd, check=True)
    return {'status': 'completed'}