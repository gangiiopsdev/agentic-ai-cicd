from fastapi import FastAPI
import subprocess
def escape_user_input(user_input):
    return user_input.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = escape_user_input(host)
    subprocess.call(f'ping {safe_host}', shell=True)
    return {'status': 'completed'}