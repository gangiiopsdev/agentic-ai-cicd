from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host):
    try:
        command = ['ping', '-c', '1'] + shlex.split(host)
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}