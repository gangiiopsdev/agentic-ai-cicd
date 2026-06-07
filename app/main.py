from fastapi import FastAPI
import subprocess
call_args = ['ping', host]
subprocess.run(call_args, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    subprocess.call(['ping', host])
    return {'status': 'completed'}