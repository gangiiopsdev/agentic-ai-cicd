from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        args = ['ping', host]
        if 'win32' in subprocess.run(['uname'], capture_output=True, text=True).stdout.lower():
            args.insert(1, '-n')
        subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)