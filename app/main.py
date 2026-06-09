from fastapi import FastAPI
import subprocess
global_args = ['ping', '127.0.0.1'] # Replace '127.0.0.1' with the desired default host

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safer implementation
    subprocess.call(global_args + [host])
    return {'status': 'completed'}