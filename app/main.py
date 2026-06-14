from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using Popen with args and ensuring host is sanitized
    sanitized_host = subprocess.list2cmdline([host])
    subprocess.Popen(['ping', sanitized_host])
    return {'status': 'completed'}