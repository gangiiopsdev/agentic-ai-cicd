from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using check_output with shell=False and proper quoting
    result = subprocess.check_output(['ping', shlex.quote(host)], stderr=subprocess.STDOUT)
    return {'status': 'completed', 'result': result.decode('utf-8')}