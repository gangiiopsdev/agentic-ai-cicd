from fastapi import FastAPI
import subprocess
global_subprocess = subprocess.Popen(['ping'], stdin=subprocess.PIPE)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    global global_subprocess
    if host:
        global_subprocess.stdin.write(f' {host}
'.encode('utf-8'))
        global_subprocess.stdin.flush()
        return {'status': 'completed'}
    else:
        return {'error': 'No host provided'}, 400