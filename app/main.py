from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Replace ping with a safe alternative that does not use shell=True
        output = subprocess.check_output(['ping', '-c', '1', host], universal_newlines=True, stderr=subprocess.STDOUT)
        return output
    except subprocess.CalledProcessError as e:
        return str(e.output)

def get_safe_ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return get_safe_ping(host)