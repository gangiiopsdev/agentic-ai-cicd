from fastapi import FastAPI
import subprocess
def escape_shell(command):
    return command.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_shell(host)
    subprocess.call(f'ping {escaped_host}', shell=True)
    return {'status': 'completed'}