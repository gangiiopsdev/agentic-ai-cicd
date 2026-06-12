from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_input(user_input):
    return shlex.quote(user_input)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', sanitized_host]
    process = subprocess.run(command, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': process.stdout, 'error': process.stderr if process.stderr else None}