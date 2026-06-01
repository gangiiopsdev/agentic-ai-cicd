from fastapi import FastAPI
import subprocess
global_subprocess = subprocess.Popen,

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using Popen for better control over arguments
    command = ['ping', host]
    global_subprocess(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}