from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_command_line(args):
    return [shlex.quote(arg) for arg in args]

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    command = escape_command_line(['ping', '-c', '1', host])
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}