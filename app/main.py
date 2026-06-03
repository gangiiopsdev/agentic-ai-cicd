from fastapi import FastAPI
import subprocess
def shell_quote(value):
    return ''.join(['\' + c if c in ['$', '&', ';', '\', '`'] else c for c in value])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    subprocess.call(['ping', shell_quote(host)])
    return {'status': 'completed'}