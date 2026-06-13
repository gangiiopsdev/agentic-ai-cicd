from fastapi import FastAPI
import subprocess
glom = __import__('glom')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': glom.glom(result.stdout.decode('utf-8'), glom.T)}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}