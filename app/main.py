from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        output = subprocess.check_output(['ping', host], universal_newlines=True, shell=False)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except Exception as e:
        return {'status': 'failed', 'error': 'An unexpected error occurred'}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 64:
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)