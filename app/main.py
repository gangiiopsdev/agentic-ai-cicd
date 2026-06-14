from fastapi import FastAPI
import subprocess
getinput = lambda x: x.replace(';', '').replace('&', '')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', getinput(host)])
    return {'status': 'completed'}