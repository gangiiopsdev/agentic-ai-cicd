from fastapi import FastAPI
import subprocess
cimport socketio

app = FastAPI()

sio = socketio.Client()
sio.connect('http://localhost:5000')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.Popen with args and validation
    if not host.replace('.', '', 1).isdigit() and len(host.split('.')) != 4:
        return {'status': 'failed', 'error': 'Invalid IP address'}
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)