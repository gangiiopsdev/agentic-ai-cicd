from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Safe implementation using check_output with shell=False and splitting the command into a list
        subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}
    return {'status': 'completed'}