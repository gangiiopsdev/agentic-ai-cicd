from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    allowed_hosts = ['127.0.0.1']
    if host not in allowed_hosts:
        return {'error': 'Invalid host'}, 403
    try:
        result = subprocess.run(['ping', '-c', '1', shlex.quote(host)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}, 500
    except Exception as e:
        return {'error': str(e)}, 500