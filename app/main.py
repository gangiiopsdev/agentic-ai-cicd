from fastapi import FastAPI
import subprocess
cimport subprocess as sp

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call and avoid shell=True
        result = sp.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except sp.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}