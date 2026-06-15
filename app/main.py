from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to prevent command injection
    if not host.replace('.', '').isdigit() or len(host.split('.')) != 4:
        return {'status': 'failed', 'error': 'Invalid IP address'}
    return execute_ping(host)