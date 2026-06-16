from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Sanitize the host input to prevent shell injection
        safe_host = shlex.quote(host)
        process = subprocess.Popen(['ping', safe_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return {'status': 'completed', 'output': output.decode(), 'error': error.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}