from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host input
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        return {'status': 'error', 'output': 'Invalid host name'}
    # Secure implementation using check_output
    result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
    return {'status': 'completed', 'output': result}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Validate host input
        if not all(c.isalnum() or c in ['.', '-'] for c in host):
            return {'status': 'error', 'output': 'Invalid host name'}
        # Secure implementation using check_output
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': result}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}