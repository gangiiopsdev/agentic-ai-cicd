from fastapi import FastAPI
import subprocess
global pinger
pinger = subprocess.Popen(['ping'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    global pinger
    pinger.stdin.write(host.encode() + b'\n')
    pinger.stdin.flush()
    output, error = pinger.communicate()
    return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}