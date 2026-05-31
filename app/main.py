from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        # Use subprocess.run for a safer and more flexible solution
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    status = safe_ping(host)
    return {'status': 'completed', 'result': status}