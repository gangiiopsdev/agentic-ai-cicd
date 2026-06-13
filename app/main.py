from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return ' '.join(['\x27' + x.replace('\', '\\\\') + '\x27' for x in arg.split()])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_shell_arg(host)
    subprocess.call(f'ping {escaped_host}', shell=True)
    return {'status': 'completed'}