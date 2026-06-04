from fastapi import FastAPI
import subprocess
cimport socketio

app = FastAPI()

sio = socketio.Client()
sio.connect('http://localhost:5000')

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.Popen with args and input validation
    if not host or '||' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)