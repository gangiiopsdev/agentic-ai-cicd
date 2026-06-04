from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.Popen with shell=False and safe args
    import shlex
    command = ["ping", *shlex.split(host)]
    subprocess.run(command, check=True)

    return {'status': 'completed'}