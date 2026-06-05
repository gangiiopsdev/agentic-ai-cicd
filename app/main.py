from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not all(char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for char in host):
        raise ValueError('Invalid hostname')
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}