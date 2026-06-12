from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate user input
    if not host.isdigit() or len(host) > 15:
        return {'status': 'error', 'message': 'Invalid host input'}

    try:
        output = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}