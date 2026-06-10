from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_argument(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    escaped_host = shlex.quote(host)
    subprocess.run(['ping', escaped_host], check=True, shell=False)
    return {'status': 'completed'}