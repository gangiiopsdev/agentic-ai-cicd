from fastapi import FastAPI
import subprocess
import shlex

git_url = 'https://github.com/example/repo.git'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with validation and proper usage of subprocess
    allowed_hosts = ['127.0.0.1', 'localhost']  # Example allowed hosts
    if host in allowed_hosts:
        try:
            command = ['ping', '-c', '4'] + shlex.split(host)
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}
    else:
        return {'status': 'unauthorized'}