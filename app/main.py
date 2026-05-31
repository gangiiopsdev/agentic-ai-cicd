from fastapi import FastAPI
import subprocess
def execute_ping(host: str):
    # Validate the host input to ensure it does not contain malicious characters
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return execute_ping(host)

# Function to validate the host input
def validate_host(host: str) -> bool:
    # Simple validation example, can be enhanced based on requirements
    return all(c.isalnum() or c in ['.', '-'] for c in host)