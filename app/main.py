from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Use check_output instead of call and avoid shell=True for security
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': result.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent shell injection
    if not host.isalnum() or ' ' in host:
        return {'status': 'failed', 'error': 'Invalid hostname'}
    return safe_ping(host)