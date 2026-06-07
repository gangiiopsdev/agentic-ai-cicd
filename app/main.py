from fastapi import FastAPI
import subprocess
global ping_mutex = threading.Lock()

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    with ping_mutex:
        try:
            response = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'response': response.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}