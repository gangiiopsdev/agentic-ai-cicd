from fastapi import FastAPI
import subprocess
global pinger
pinger = subprocess.Popen(['ping', 'example.com'], stdout=subprocess.PIPE)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    global pinger
    if host == 'example.com':  # Add validation for the input
        pinger.terminate()
        pinger.wait()
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400