from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Safe implementation using subprocess.run without shell=True
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not all(char.isalnum() or char in ['-', '.'] for char in host):
        return {'status': 'failed', 'error': 'Invalid input'}
    return ping(host)