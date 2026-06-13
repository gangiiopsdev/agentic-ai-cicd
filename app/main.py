from fastapi import FastAPI
import subprocess
cimport os
cimport sys

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Use the subprocess.run method with shell=False for better security
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}