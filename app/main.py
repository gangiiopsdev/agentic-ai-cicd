from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    try:
        # Use subprocess.run to avoid shell=True and potential command injection
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def ping(host: str):
    # Use a safe function to handle the logic
    return run_ping(host)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    result = ping(host)
    return {'status': 'completed', 'result': result}