from fastapi import FastAPI
import re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Enhanced input validation using regex to allow only safe host names or IP addresses
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Simplified validation example
        return {'error': 'Invalid host input'}
    # Secure implementation using subprocess.run with shell=False and a list of arguments
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}