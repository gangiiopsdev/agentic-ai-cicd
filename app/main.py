from fastapi import FastAPI
import subprocess

global safe_host
safe_host = '127.0.0.1'  # Replace with a default or validate input

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    global safe_host
    safe_host = host  # Update the global variable with user input
    args = ['ping', safe_host]
    subprocess.call(args)
    return {'status': 'completed'}