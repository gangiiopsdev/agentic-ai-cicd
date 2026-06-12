from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with input validation
    if not host.isalnum():
        raise ValueError('Invalid input')
    subprocess.run(['ping', host], check=True, shell=False)

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        return {'result': ping(host)}
    except Exception as e:
        return {'error': str(e)}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}