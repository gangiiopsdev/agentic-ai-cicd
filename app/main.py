from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        ip_address = subprocess.check_output(['nslookup', host], stderr=subprocess.STDOUT).decode('utf-8').splitlines()[2].strip().split()[-1]
        subprocess.call(['ping', '-c', '4', ip_address])
        return {'status': 'completed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}