from fastapi import FastAPI
import subprocess
global_result = ''

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    global_result = subprocess.call(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'result': global_result}