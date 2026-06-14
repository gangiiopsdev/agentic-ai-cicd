from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_subprocess(command, *args):
    try:
        result = subprocess.run([command] + list(args), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode(), result.stderr.decode()
    except subprocess.CalledProcessError as e:
        return None, e.stderr.decode()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    stdout, stderr = safe_subprocess('ping', host)
    if stdout:
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'error': stderr}