from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize input to prevent injection attacks
        if not host.replace('.', '').replace('-', '').isdigit() and '-' not in host:
            raise ValueError('Invalid hostname')
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except ValueError as ve:
        return {'status': 'failed', 'error': str(ve)}