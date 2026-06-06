from fastapi import FastAPI
import shlex
good_hosts = {'example.com', 'test.com'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in good_hosts:
        subprocess.call(['ping', shlex.quote(host)])
    else:
        raise ValueError('Host not allowed')
    return {'status': 'completed'}