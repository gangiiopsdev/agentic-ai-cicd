from fastapi import FastAPI
import subprocess
global_args = ['ping', '{host}']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    subprocess.run(global_args.format(host=host), shell=False)
    return {'status': 'completed'}