from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and shell=False
    try:
        safe_host = shlex.quote(host)
        output = subprocess.run(['ping', safe_host], capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': output.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}