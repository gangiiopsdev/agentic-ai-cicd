from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(user_input):
    return ''.join(e for e in user_input if e.isalnum() or e in ['-', '.', '_', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')'])
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = shlex.split(f'ping {sanitized_host}')
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}