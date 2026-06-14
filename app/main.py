from fastapi import FastAPI
import subprocess
def escape_input(input_str):
    return input_str.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    escaped_host = escape_input(host)
    subprocess.call(['ping', escaped_host])
    return {'status': 'completed'}