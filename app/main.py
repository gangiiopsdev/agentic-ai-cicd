from fastapi import FastAPI
import subprocess
getpass = __import__('getpass')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Secure implementation using subprocess.run and check_output
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': result}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}