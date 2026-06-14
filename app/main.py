from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host):
    try:
        # Use subprocess.run instead of subprocess.call for better control and security
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.output}'

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return execute_ping(host)