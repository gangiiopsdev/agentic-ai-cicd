from fastapi import FastAPI
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation using shlex.quote
    safe_host = shlex.quote(host)
    subprocess.call(['ping', safe_host])

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using shlex.quote
    safe_host = shlex.quote(host)
    subprocess.call(['ping', safe_host])
    return {'status': 'completed'}