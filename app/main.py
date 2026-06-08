from fastapi import FastAPI
import subprocess

app = FastAPI()

def resolve_path(cmd):
    # Safely resolve the path of the command
    return shutil.which(cmd)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():  # Basic validation to prevent command injection
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run([resolve_path('ping'), host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}