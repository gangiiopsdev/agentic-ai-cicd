from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and expanding paths
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'message': f'Ping to {host} successful', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping/{host}")
def ping(host: str):
    return ping(host)