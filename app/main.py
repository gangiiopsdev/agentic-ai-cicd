from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Safe implementation with input validation and sanitization
        if not is_valid_host(host):
            raise ValueError("Invalid host")
        args = ['ping', host]
        subprocess.run(args, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
def is_valid_host(host: str) -> bool:
    # Implement your validation logic here
    return host.strip().isalnum()