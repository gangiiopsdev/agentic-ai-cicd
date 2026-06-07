from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input to prevent command injection
        if not validate_host(host):
            raise ValueError('Invalid host input')
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}
def validate_host(host: str) -> bool:
    # Add your validation logic here
    allowed_hosts = ['example.com', 'test.example.com']
    return host in allowed_hosts