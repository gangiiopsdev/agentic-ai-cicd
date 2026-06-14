from fastapi import FastAPI
import subprocess
global_args = ['ping', '-c', '1']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    global_args.append(host)
    subprocess.call(global_args)
    return {'status': 'completed'}