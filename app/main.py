from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_subprocess(command: list) -> None:
    try:
        result = subprocess.run(command, check=True, capture_output=True)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(e.stderr.decode())

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = subprocess.shlex_quote(host)
    command = ['ping', safe_host]
    safe_subprocess(command)
    return {'status': 'completed'}