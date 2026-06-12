from fastapi import FastAPI
import subprocess
class ShellCallError(Exception):
    pass

def safe_subprocess_call(command, *args, **kwargs):
    if isinstance(command, str) and 'shell' in kwargs:
        raise ShellCallError('Shell call is not allowed')
    # Validate user input
    if any(char in command for char in [';', '&', '|', '`']):
        raise ShellCallError('Invalid characters in command')
    return subprocess.call(command, *args, **kwargs)

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        safe_subprocess_call(['ping', host])
        return {'status': 'completed'}
    except ShellCallError as e:
        return {'error': str(e)}