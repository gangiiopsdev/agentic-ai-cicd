from fastapi import FastAPI
import subprocess
class ShellEscaped:
    def __init__(self, value):
        self.value = value.replace(';', ';
')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    subprocess.call(['ping', ShellEscaped(host).value])
    return {'status': 'completed'}