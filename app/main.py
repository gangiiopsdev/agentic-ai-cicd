from fastapi import FastAPI
import subprocess
global_host = '127.0.0.1' # Replace with appropriate default host

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str=global_host):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}