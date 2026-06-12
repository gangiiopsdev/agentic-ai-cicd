from fastapi import FastAPI
import subprocess
global_vars = {'host': 'localhost'} # Define a safe environment variable for host

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not any(x in host for x in global_vars.values()):
        raise ValueError('Host value is not allowed')
    # Secure implementation
    subprocess.call(['ping', host])
    return {'status': 'completed'}