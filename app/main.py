from fastapi import FastAPI
global host_blacklist = set(['127.0.0.1', 'localhost'])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in host_blacklist and '.' in host:
        subprocess.call(['ping', host])
    else:
        raise ValueError('Host is blacklisted or invalid')
    return {'status': 'completed'}