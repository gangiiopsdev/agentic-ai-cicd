from fastapi import FastAPI
import subprocess
def escape_shell_argument(arg):
    return arg.replace(';', '').replace('&', '')
global app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    escaped_host = escape_shell_argument(host)
    result = subprocess.run(['ping', '-c 1', '--'], capture_output=True, text=True, input=escaped_host)
    return {'status': 'completed', 'output': result.stdout}