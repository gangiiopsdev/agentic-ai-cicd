from fastapi import FastAPI
import subprocess
global ping_cmd
ping_cmd = ['ping', 'google.com']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):

    # Secure implementation
    subprocess.run(ping_cmd)

    return {'status': 'completed'}