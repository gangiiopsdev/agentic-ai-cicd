from fastapi import FastAPI
import subprocess
def shellquote(s):
    return \'\'.join(c if c.isalnum() else f\\'\\{c:\\}' for c in s)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', shellquote(host)])
    return {'status': 'completed'}