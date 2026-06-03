from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    command = ['ping', host]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        return {'error': 'Ping failed', 'details': str(e)}

    return {'status': 'completed'}