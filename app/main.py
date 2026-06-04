from fastapi import FastAPI
import subprocess
global_result = None
def ping(host: str):
    global global_result
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        global_result = result.stdout
    except Exception as e:
        global_result = f'Error: {str(e)}'
    return {'status': 'completed'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_wrapper(host: str):
    return ping(host)