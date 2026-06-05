from fastapi import FastAPI
import subprocess
gateway = subprocess.Popen(['ping', '{}'.format(host)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = gateway.communicate()
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    if not host.isalnum():  # Simple validation to allow only alphanumeric characters
        return {'error': 'Invalid input'}, 400
    gateway = subprocess.Popen(['ping', '{}'.format(host)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = gateway.communicate()
    return {'status': 'completed', 'output': stdout.decode()}