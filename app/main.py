from fastapi import FastAPI
import subprocess
import os

cwd = os.getcwd()
app = FastAPI()

def sanitize_input(input_string):
    # Implement input sanitization logic here
    return ''.join(filter(str.isalnum, input_string))

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent code injection
    sanitized_host = sanitize_input(host)
    subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True, cwd=cwd)
    return {'status': 'completed'}