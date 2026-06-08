from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(user_input):
    return ''.join(e for e in user_input if e.isalnum() or e.isdigit() or e in ['.', '-', '_', '@', '!', '#', '$', '%', '&', '*', '+', '=', '?', '^', '`', '{', '|', '}', '~'])

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    return {'status': 'completed', 'output': output.decode()}