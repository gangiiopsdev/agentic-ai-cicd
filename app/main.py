from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Safe implementation using subprocess.run with check_output and capturing output
        output = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)