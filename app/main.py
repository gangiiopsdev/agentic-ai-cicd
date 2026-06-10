from fastapi import FastAPI
import subprocess
git_command = ['ping', host]
subprocess.call(git_command)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    subprocess.call(['ping', host])
    return {'status': 'completed'}