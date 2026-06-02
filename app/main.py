from fastapi import FastAPI
import subprocess
getoutput = subprocess.getoutput

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        result = getoutput(f'ping {host}')
        return {'status': 'completed', 'result': result}
    except Exception as e:
        return {'error': str(e), 'status': 'failed'}