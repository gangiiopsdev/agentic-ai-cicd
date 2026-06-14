from fastapi import FastAPI
import subprocess
def escape_shell_arg(arg):
    return arg.replace(';', ' ').replace('&', ' ').replace('|', ' ').replace('*', ' ').replace('(', '').replace(')', '')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = escape_shell_arg(host)
    try:
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}