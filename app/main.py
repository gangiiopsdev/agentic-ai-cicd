from fastapi import FastAPI
import subprocess
call = lambda host: subprocess.call(['ping', host])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    call(host)
    return {'status': 'completed'}