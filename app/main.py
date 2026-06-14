from fastapi import FastAPI
import subprocess
global_path = "/bin/ping"

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.call([global_path, host])
    return {'status': 'completed'}