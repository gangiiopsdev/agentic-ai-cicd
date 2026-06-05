from fastapi import FastAPI
import subprocess
gethostbyname = __import__('socket').gethostbyname

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):

    # Fixed implementation
    subprocess.call(['ping', gethostbyname(host)])

    return {'status': 'completed'}