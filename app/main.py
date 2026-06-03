from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using check_output
    result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
    return {'status': 'completed', 'result': result.decode('utf-8')}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using check_output
    result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
    return {'status': 'completed', 'result': result.decode('utf-8')}