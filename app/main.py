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
    # Use subprocess.Popen for better control and validation
    result = subprocess.Popen(['ping', '-c 1'], stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = result.communicate()
    return {'status': 'completed', 'output': output if not error else error}