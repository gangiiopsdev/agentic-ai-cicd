from fastapi import FastAPI
import subprocess
def escape_host(host):
    # Simple escaping to prevent shell injection
    return host.replace(';', '').replace('&', '').replace('||', '')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with basic input escaping
    subprocess.call(['ping', escape_host(host)], shell=False)
    return {'status': 'completed'}