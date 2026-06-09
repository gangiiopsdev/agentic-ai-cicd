from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        # Using check_output to avoid shell injection and ensure the command is executed safely
        result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f'Ping failed with error: {e.output}'

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)