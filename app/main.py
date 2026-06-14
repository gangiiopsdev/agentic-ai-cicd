from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host in ['google.com', 'bing.com']:  # Example allowed hosts
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
            return {'status': 'completed', 'output': output.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode()}
        except subprocess.TimeoutExpired:
            return {'status': 'timed out'}
    else:
        return {'status': 'failure', 'message': 'Invalid host'}