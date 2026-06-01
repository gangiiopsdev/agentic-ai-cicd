from fastapi import FastAPI
import subprocess
global_process = None

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    global global_process
    if global_process is not None:
        global_process.terminate()
        global_process.wait()
    try:
        process = subprocess.Popen(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        global_process = process
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}