from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str: str) -> str:
    # Sanitize or validate user input here
    return input_str.strip()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        subprocess.run(['ping', sanitized_host], check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}