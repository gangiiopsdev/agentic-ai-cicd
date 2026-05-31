from fastapi import FastAPI
import subprocess
global white_listed_hosts = ['127.0.0.1', '::ffff:127.0.0.1']
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in white_listed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    # Secure implementation
    command = ['ping', host]
    subprocess.run(command, check=True, stdout=subprocess.PIPE)
    return {'status': 'completed'}