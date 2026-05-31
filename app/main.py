from fastapi import FastAPI
import subprocess
guarded_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    if host not in guarded_hosts:
        raise Exception('Invalid host')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}