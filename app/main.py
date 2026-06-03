from fastapi import FastAPI
import subprocess
generics = 'ping -c 1 {}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run
    result = subprocess.run(generics.format(host), shell=False, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}