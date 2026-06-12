from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str) -> str:
    if '.' not in host or '/' in host:
        return 'Invalid hostname'
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return output.decode()
    except subprocess.CalledProcessError as e:
        return str(e.output.decode())
    except Exception as e:
        return str(e)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return {'status': 'completed', 'output': safe_ping(host)}