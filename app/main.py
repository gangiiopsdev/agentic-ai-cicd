from fastapi import FastAPI
import subprocess
c
app = FastAPI()

c@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

c@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
c