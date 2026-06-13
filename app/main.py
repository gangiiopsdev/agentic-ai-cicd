from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    args = ['ping', *shlex.split(host)]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_wrapper(host: str):
    return ping(host)