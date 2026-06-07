from fastapi import FastAPI
import subprocess
import string

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(filter(lambda x: x in string.printable and x.isalnum(), input_str))

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    host = sanitize_input(host)
    if not host:
        return {'status': 'failed', 'message': 'Invalid input'}
    subprocess.run(['ping', host], check=True, shell=False)
    return {'status': 'completed'}