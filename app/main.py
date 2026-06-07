from fastapi import FastAPI
import subprocess
global_host = 'example.com'  # Use a hardcoded safe value instead of user input

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess with args instead of shell=True
    result = subprocess.run(['ping', global_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}