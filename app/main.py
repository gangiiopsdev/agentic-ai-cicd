from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    if os.name == 'nt':
        args.insert(0, 'cmd.exe')
    subprocess.call(args)
    return {'status': 'completed'}