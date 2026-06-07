from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate input to prevent command injection
    if not host.strip() or '@' in host:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping")
def ping_wrapper(host: str):
    return ping(host)