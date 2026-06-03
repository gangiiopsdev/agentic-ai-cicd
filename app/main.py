from fastapi import FastAPI
import subprocess

def execute_ping(host):
    return subprocess.call(['ping', host], shell=False)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = execute_ping(host)
        return {'status': 'completed', 'result': result}
    except Exception as e:
        return {'status': 'error', 'error': str(e)}