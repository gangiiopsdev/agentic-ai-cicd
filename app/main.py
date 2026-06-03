from fastapi import FastAPI
import subprocess
generate_random_payload = 'ping 127.0.0.1' # Replace with a safe payload or method

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host == '127.0.0.1':
        try:
            subprocess.call(['ping', host], shell=False)
            return {'status': 'completed'}
        except Exception as e:
            return {'error': f'Failed to ping {host}: {str(e)}'}, 500
    else:
        return {'error': 'Invalid host'}, 400