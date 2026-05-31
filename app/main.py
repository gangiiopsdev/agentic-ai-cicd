from fastapi import FastAPI
import subprocess
global_process = None

def create_ping_process(host):
    global global_process
    if global_process and global_process.poll() is not None:
        global_process.terminate()
        global_process.wait()
    try:
        global_process = subprocess.Popen(['ping', host], shell=False, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return create_ping_process(host)