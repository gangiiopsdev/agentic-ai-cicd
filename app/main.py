from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def ping(host: str):
    try:
        # Use an absolute path for 'ping' to mitigate CWE-78
        result = subprocess.run([os.path.join('/usr/bin', 'ping'), host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stderr': e.stderr.decode()}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return ping(host)