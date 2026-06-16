from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Constructing the command safely
    cmd = ['ping', host]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error {e}')
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}