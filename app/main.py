from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')</code><br>
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host not in ['localhost', '127.0.0.1']:
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}