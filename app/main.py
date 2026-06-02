from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    # Use subprocess.run for safer execution
    args = ['ping', host]
    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return result.stdout.decode('utf-8')

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}