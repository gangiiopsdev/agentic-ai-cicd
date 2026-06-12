from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get('/safe-ping')
def safe_ping(host: str):
    # Safe implementation using ping3 library
    try:
        import ping3
        response = ping3.ping(host, timeout=5)
        if response is not None:
            return {'status': 'completed', 'response_time': response}
        else:
            return {'status': 'failed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}