from fastapi import FastAPI
import subprocess
def secure_ping(host: str):
    # Secure implementation using shlex.quote to escape special characters in the host input.
    from shlex import quote
    subprocess.call(['ping', quote(host)])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    secure_ping(host)
    return {'status': 'completed'}