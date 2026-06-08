from fastapi import FastAPI
import subprocess
gt = 'ping {}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    completed_process = subprocess.run(gt.format(host), shell=False, capture_output=True, text=True)
    return {'status': 'completed', 'output': completed_process.stdout}