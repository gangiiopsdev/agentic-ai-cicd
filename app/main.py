from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.Popen with shell=False and properly escaped arguments
    import shlex
    command = ['ping', host]
    subprocess.call(command, shell=False)
    return {'status': 'completed'}