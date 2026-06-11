from fastapi import FastAPI
import subprocess
def sanitize_input(input_string):
    return ''.join(char for char in input_string if char.isalnum() or char in ('.', '-', '_'))

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = sanitize_input(host)
    # Use check_output instead of call for better error handling and output capture
    try:
        subprocess.check_output(['ping', '-c', '1', safe_host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}