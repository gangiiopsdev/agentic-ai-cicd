from fastapi import FastAPI
import subprocess
def secure_ping(host: str):
    # Use shlex.quote to escape special characters in the input
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', safe_host])
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    return secure_ping(host)