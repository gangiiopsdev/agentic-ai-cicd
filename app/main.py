from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Replace ping with a safe alternative that does not use shell=True
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=False)
        return output.stdout or output.stderr
    except Exception as e:
        return str(e)

def get_safe_ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return get_safe_ping(host)