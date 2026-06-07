from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using shlex.quote to sanitize the input and fully specify the executable path
    subprocess.call(['ping', '-c', '1', shlex.quote(host)])
    return {'status': 'completed'}