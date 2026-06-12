from fastapi import FastAPI
import subprocess
def escape_shell(input_string):
    return input_string.replace(';', '').replace('&', '').replace('&&', '').replace('|', '')
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    safe_host = escape_shell(host)
    subprocess.run(['ping', safe_host], check=True, capture_output=True)
    return {'status': 'completed'}