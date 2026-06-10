from fastapi import FastAPI
import subprocess
def sanitize_input(user_input):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    sanitized = ''.join(char for char in user_input if char in allowed_chars)
    return sanitized

cmd = ['ping', sanitized_host]
subprocess.run(cmd, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    cmd = ['ping', sanitized_host]
    subprocess.run(cmd, check=True)
    return {'status': 'completed'}