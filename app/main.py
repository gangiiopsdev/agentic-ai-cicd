from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Enhanced input validation and use of safe alternatives
    if all(c.isalnum() or c in ('-', '.', '_') for c in host):  # Basic validation of the hostname
        try:
            result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}, 500
    else:
        return {'error': 'Invalid hostname'}, 400