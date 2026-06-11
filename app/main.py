from fastapi import FastAPI
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with validation
    if not host.isalnum() and '-' not in host:
        return {'status': 'invalid input'}
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}