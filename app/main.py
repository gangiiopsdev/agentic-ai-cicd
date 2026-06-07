from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation with full path and avoiding shell=True
    try:
        subprocess.run(['/bin/ping', '-c', '1', host], check=True, text=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}

@app.get="/"
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get="/ping"
def ping(host: str):
    # Secure implementation with full path and avoiding shell=True
    try:
        subprocess.run(['/bin/ping', '-c', '1', host], check=True, text=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}