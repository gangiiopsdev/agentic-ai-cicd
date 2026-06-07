from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    args = ['ping', host]
    sanitized_args = [shlex.quote(arg) for arg in args]
    subprocess.call(sanitized_args)
    return {'status': 'completed'}