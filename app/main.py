from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    if host in allowed_hosts:
        return True
    return False

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if validate_host(host):
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400