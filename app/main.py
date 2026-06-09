from fastapi import FastAPI
import subprocess
given_host = '127.0.0.1' # replace with a safe default or input validation
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    subprocess.call(['ping', given_host])
    return {'status': 'completed'}