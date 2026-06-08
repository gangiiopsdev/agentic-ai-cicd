from fastapi import FastAPI
import subprocess
gitpython from subprocess import Popen, PIPE

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    process = Popen(['ping', host], stdout=PIPE, stderr=PIPE)
    output, error = process.communicate()
    return {'status': 'completed'}