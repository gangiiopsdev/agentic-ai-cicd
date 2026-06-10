from fastapi import FastAPI
import subprocess
global ping_command
ping_command = 'ping {}'

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation without shell=True
    subprocess.run(ping_command.format(host), shell=False, check=True)
    return {'status': 'completed'}