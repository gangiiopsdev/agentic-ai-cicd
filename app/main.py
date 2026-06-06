from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation with full path and avoiding shell=True
    subprocess.call(['/bin/ping', '-c', '1', host])
    return {'status': 'completed'}

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with full path and avoiding shell=True
    subprocess.call(['/bin/ping', '-c', '1', host])
    return {'status': 'completed'}