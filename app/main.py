from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with shlex.quote to escape special characters in the input
    subprocess.run(['ping', shlex.quote(host)], check=True)
    return {'status': 'completed'}