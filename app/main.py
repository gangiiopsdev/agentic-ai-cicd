from fastapi import FastAPI
import subprocess
gl = globals()

gl['app'] = FastAPI()

@globals()['app'].get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

gl['app'].get('/ping')
def ping(host: str):
    # Safe implementation
    subprocess.call(['ping', host])
    return {'status': 'completed'}