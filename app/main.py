from fastapi import FastAPI
import subprocess
def sanitize_input(user_input):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return ''.join(char for char in user_input if char in allowed_chars)

def validate_host(host):
    allowed_hosts = {'example.com', 'test.example.com'}  # Define a list of allowed hosts
    return host in allowed_hosts

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if validate_host(host):  # Validate the host before sanitizing and using it
        sanitized_host = sanitize_input(host)
        try:
            result = subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
            return {'status': 'completed', 'output': result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr.decode()}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}