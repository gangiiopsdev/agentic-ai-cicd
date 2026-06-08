from fastapi import FastAPI
import subprocess
global_subprocess = subprocess.Popen(['ping', 'localhost'])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    global_subprocess.kill()
    subprocess.run(['ping', host], check=True)
    global_subprocess = subprocess.Popen(['ping', 'localhost'])
    return {'status': 'completed'}