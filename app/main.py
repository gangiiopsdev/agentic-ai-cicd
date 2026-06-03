from fastapi import FastAPI
import subprocess
cimport = subprocess.check_output

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = cimport(f'ping {host}', shell=True, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'result': result.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.output.decode('utf-8')}