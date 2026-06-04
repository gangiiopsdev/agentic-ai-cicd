from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Secure implementation using subprocess.run with shell=False and safe arguments
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

# Preventive controls:
# 1. Validate and sanitize user input to ensure it does not contain malicious content.
# 2. Use a whitelist of allowed hosts if possible.
# 3. Avoid using shell=True when calling subprocess.run.