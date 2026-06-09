from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(e for e in input_string if e.isalnum() or e in ['.', '-', '_'])

cmd = f'ping {sanitize_input(host)}'
subprocess.call(cmd, shell=False)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    subprocess.run(['ping', sanitize_input(host)], check=True)
    return {'status': 'completed'}