from fastapi import FastAPI
import subprocess
global pinger
pinger = subprocess.Popen(['ping', '-c', '1'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    pinger.stdin.write(f'{host}
'.encode())
    pinger.stdin.close()
    output, error = pinger.communicate()
    if pinger.returncode == 0:
        return {'status': 'completed', 'output': output.decode()}
    else:
        return {'status': 'failed', 'error': error.decode()}